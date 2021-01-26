from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from bson.objectid import ObjectId
from datetime import datetime
import random
import json
import pymongo
import ssl

from address.address import createAddress 
from person.person import createPerson
from worker.worker import createWorker
from jobApplicant.createJobApplicant import createJobApplicant 
from jobRequisition.jobRequisition import createJobRequisition
from jobApplicant.PreviousEmployer import newEmployerName

class Encoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, ObjectId):
      return str(obj)
    if isinstance(obj, datetime):
      return str(obj)
    else:
      raise TypeError(f"Unserializable object {obj} of type {type(obj)}")

connection_url = 'mongodb+srv://relianceAdmin:rjr1234!@cluster0.lx0nm.mongodb.net/hcm?retryWrites=true&w=majority'
cors_string = 'Access-Control-Allow-Origin'
app = Flask(__name__)
cors_app = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
client = pymongo.MongoClient(connection_url, ssl_cert_reqs=ssl.CERT_NONE)

db = client.get_database('hcmData')

completeTable = {}
company = newEmployerName()

def replaceObjectId(response):
  response['_id'] = str(response['_id'])
  return response

def changeDbName(dbName):
  global db
  db = client.get_database(dbName)

@app.route('/api/changeDB', methods=['POST'])
def changeDB():
  dbName = request.get_json()['dbName']
  changeDbName(dbName)
  resp = jsonify(success=True)
  return resp

@app.route('/api/getdbnames', methods=['GET'])
def getDBs():
  databases = []
  for database in client.list_database_names():
    databases.append(database)
  databases = list(filter(lambda x: x != 'admin' and x != 'local', databases))
  resp = jsonify(databases)
  return resp

@app.route('/api/address', methods=['GET'])
def getAddress():
  singleState = list(db.address.aggregate([{ "$sample": { "size": 1 }}]))[0]
  singleState = json.dumps(singleState, cls=Encoder) 
  singleState = jsonify(singleState)
  return singleState

@app.route('/api/person', methods=['GET'])
def getPerson():
  singlePerson = list(db.person.aggregate([{ "$sample": { "size": 1 }}]))[0]
  singlePerson = json.dumps(singlePerson, cls=Encoder) 
  singlePerson = jsonify(singlePerson)
  return singlePerson 
  
@app.route('/api/jobRequisition', methods=['GET'])
def getJobReq():
  singleJobReq = list(db.jobRequisitions.aggregate([{ "$sample": { "size": 1 }}]))[0]
  singleJobReq = json.dumps(singleJobReq, cls=Encoder)
  singleJobReq = jsonify(singleJobReq)
  return singleJobReq
  
@app.route('/api/jobApplicant', methods=['GET'])
def getJobApplicant():
  singleJobApplicant = list((db.jobApplicants.aggregate([{ "$sample": { "size": 1 }}])))[0]
  singleJobApplicant = json.dumps(singleJobApplicant, cls=Encoder)
  singleJobApplicant = jsonify(singleJobApplicant)
  return singleJobApplicant

@app.route('/api/worker', methods=['GET'])
def getWorker():
  singleWorker = list(db.worker.aggregate([{ "$sample": { "size": 1 }}]))[0]
  singleWorker = json.dumps(singleWorker, cls=Encoder)
  singleWorker = jsonify(singleWorker)
  return singleWorker 

@app.route('/api/newDB', methods=['POST'])
def newDB():
  global db
  dbName = db.name
  client.drop_database(dbName)
  db = client[dbName]

  completeTable["addresses"] = []
  completeTable["people"] = []
  completeTable["workers"] = []
  completeTable["jobRequisitions"] = []
  completeTable["jobApplicants"] = []

  # Initialize spiked fields from request
  spikedData = {}
  spikedData["companyName"] = request.get_json()['companyName']
  spikedData["addrInfo"] = request.get_json()['addrInfo']
  spikedData["age"] = request.get_json()['age']
  spikedData["ethnicity"] = request.get_json()['ethnicity']
  spikedData["gender"] = request.get_json()['gender']
  spikedData["workerTypes"] = request.get_json()['workerTypes']
  spikedData["fullTimeEquivalency"] = request.get_json()['fullTimeEquivalency']


  generateHierarchy(spikedData)
  
  db["address"].insert_many(completeTable["addresses"])
  db["person"].insert_many(completeTable["people"])
  db["worker"].insert_many(completeTable["workers"])
  db["jobRequisitions"].insert_many(completeTable["jobRequisitions"])
  db["jobApplicants"].insert_many(completeTable["jobApplicants"])

  resp = jsonify(success=True)
  return resp

#
# @func   generateHierarchy
# @desc   Generates CEO, and from there calls the recursive function generateFieldData for each department 
#         operating under the CEO 
# @param  city, state object
#
def generateHierarchy(spikedData):
  # Marketing, Finance, IT, Operations, HR
  # Recursively generate from CEO down

  generateEmployee(spikedData, "CEO", None, 0)
  CEO = {}
  CEO["name"] = completeTable["people"][0]["address"]["nameCode"]
  CEO["positionTitle"] = "CEO"

  finances = ["CFO", "President of Finance", "Vice-President of Finance", "Senior Finance Officer", "Senior Finance Manager", "Finance Manager", "Lead Finance Associate", "Finance Associate"]
  it = ["CTO", "President of Information Technology", "Vice-President of Information Technology", "Senior Information Technology Officer", "Senior Information Technology Manager", "Information Technology Manager", "Lead Information Technology Associate", "Information Technology Associate"]
  marketing = ["President of Marketing", "Vice-President of Marketing", "Senior Marketing Officer", "Senior Marketing Manager", "Marketing Manager", "Lead Marketing Associate", "Marketing Associate"]
  operations = ["COO", "President of Operations", "Vice-President of Operations", "Senior Operations Officer", "Senior Operations Manager", "Operations Manager", "Lead Operations Associate", "Operations Associate"]
  hr = ["President of Human Resources", "Vice-President of Human Resources", "Senior Human Resources Officer", "Senior Human Resources Manager", "Human Resources Manager", "Lead Human Resources Asscociate", "Human Resources Asscociate"]

  generateFieldData(spikedData, finances, CEO, 0)
  generateFieldData(spikedData, it, CEO, 0)
  generateFieldData(spikedData, marketing, CEO, 0)
  generateFieldData(spikedData, operations, CEO, 0)
  generateFieldData(spikedData, hr, CEO, 0)

#
# @func   generateFieldData
# @desc   Recursively generates employee data based on positions and supervisors passed down
# @param  positions for a given department in order of highest to lowest superiority, supervisor object, depth from highest position
#
def generateFieldData(spikedData, positions, supervisor, depth):

  if not positions:
    return

  title = positions[0]

  if depth > 2 and len(positions) > 1:
    for _ in range(random.randrange(3, 5)):
      generateEmployee(spikedData, title, supervisor, depth)
      employee = {}
      employee["name"] = completeTable["people"][-1]["address"]["nameCode"]
      employee["positionTitle"] = title
      generateFieldData(spikedData, positions[1:], employee, depth+1)

  else:
    generateEmployee(spikedData, title, supervisor, depth)
    employee = {}
    employee["name"] = completeTable["people"][-1]["address"]["nameCode"]
    employee["positionTitle"] = title
    generateFieldData(spikedData, positions[1:], employee, depth+1)

  return

#
# @func   generateEmployee
# @desc   call items to generate each table for an employee
# @param  job title, supervisor object
#
def generateEmployee(spikedData, title, supervisor, depth):
  newPerson = createPerson(list(map(lambda x: int(x), spikedData["gender"].values())) if spikedData["gender"] else None, 
  list(map(lambda x: int(x), spikedData["age"].values())) if spikedData["age"] else None, 
  list(map(lambda x: int(x), spikedData["ethnicity"].values())) if spikedData["ethnicity"] else None)
  newAddress = createAddress(newPerson, spikedData["addrInfo"])
  newPerson["address"] = newAddress
  newWorker = createWorker(newPerson, title, supervisor, depth, {"workerTypes": list(map(lambda x: int(x), spikedData["workerTypes"].values()))} if spikedData["workerTypes"] else None)
  newWorker["workAssignment"]["legalEntityID"] = spikedData["companyName"] if spikedData["companyName"] else company
  newPerson["address"].pop("county")
  newJobRequistion = createJobRequisition(title, list(map(lambda x: int(x), spikedData["fullTimeEquivalency"].values())) if spikedData["fullTimeEquivalency"] else None )
  newJobApplicant = createJobApplicant(newPerson)

  completeTable["addresses"].append(newAddress)
  completeTable["people"].append(newPerson)
  completeTable["workers"].append(newWorker)
  completeTable["jobRequisitions"].append(newJobRequistion)
  completeTable["jobApplicants"].append(newJobApplicant)

if __name__ == "__main__":
  app.run(debug=True)
