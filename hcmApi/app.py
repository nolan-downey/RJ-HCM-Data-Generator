from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS, cross_origin
from bson.objectid import ObjectId
from datetime import datetime
import json
import pymongo

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
client = pymongo.MongoClient(connection_url)

db = client.get_database('hcmData')

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
  print(f'hitting changeDB; dbName: {db.name}')
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

@app.route('/api/addresses', methods=['GET'])
def getAddress():
  stateCode = request.args.get('stateCode')
  states = db.address.find_one({"stateCode": stateCode})
  stateToReturn = []
  states = json.dumps(states, cls=Encoder) 
  stateToReturn.append(states)
  # for state in states:
  #   state['_id'] = str(state['_id'])
  #   stateToReturn.append(state)
  stateToReturn = jsonify(stateToReturn)
  return stateToReturn
  
@app.route('/api/jobRequisitions', methods=['GET'])
def getJobReq():
  singleJobReq = list(db.jobRequisitions.aggregate([{ "$sample": { "size": 1 }}]))[0]
  singleJobReq = json.dumps(singleJobReq, cls=Encoder)
  singleJobReq = jsonify(singleJobReq)
  return singleJobReq
  
@app.route('/api/jobApplicants', methods=['GET'])
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

if __name__ == "__main__":
  app.run(debug=True)
