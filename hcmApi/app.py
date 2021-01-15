from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS, cross_origin
from flask_pymongo import PyMongo
import pymongo

connection_url = 'mongodb+srv://relianceAdmin:rjr1234!@cluster0.lx0nm.mongodb.net/hcm?retryWrites=true&w=majority'
cors_string = 'Access-Control-Allow-Origin'
app = Flask(__name__)
cors_app = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
client = pymongo.MongoClient(connection_url)

db = client.get_database('hcmData')

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
  print(db.name)
  stateCode = request.args.get('stateCode')
  states = db.address.find({"stateCode": stateCode})
  stateToReturn = []
  for state in states:
    state['_id'] = str(state['_id'])
    stateToReturn.append(state)
  stateToReturn = jsonify(stateToReturn)
  return stateToReturn

if __name__ == "__main__":
  app.run()
