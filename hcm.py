#!/usr/bin/env python3

import pymongo
import ssl
import random
from decouple import config
import pprint

from address.address import createAddress 
from person.person import createPerson
from worker.worker import createWorker
from jobApplicant.createJobApplicant import createJobApplicant 
from jobRequisition.jobRequisition import createJobRequisition 

completeTable = {}

def main():
  uri = "mongodb+srv://{user}:{password}@cluster0.lx0nm.mongodb.net/{db}?retryWrites=true&w=majority".format(user=config("USERNAME"),password=config("PASSWORD"),db=config("DB") )

  client = pymongo.MongoClient(uri, ssl_cert_reqs=ssl.CERT_NONE)
  db = client.hcmData

  completeTable["addresses"] = []
  completeTable["people"] = []
  completeTable["workers"] = []
  completeTable["jobRequisitions"] = []
  completeTable["jobApplicants"] = []

  generateHierarchy()
  
  print("Adding data to database...")
  db["address"].insert_many(completeTable["addresses"])
  db["person"].insert_many(completeTable["people"])
  db["worker"].insert_many(completeTable["workers"])
  db["jobRequisitions"].insert_many(completeTable["jobRequisitions"])
  db["jobApplicants"].insert_many(completeTable["jobApplicants"])

def generateHierarchy():
  # Marketing, Finance, IT, Operations, HR
  # Recursively generate from CEO down

  generateEmployee("CEO", None)
  CEO = {}
  CEO["name"] = completeTable["people"][0]["address"]["nameCode"]
  CEO["positionTitle"] = "CEO"

  finances = ["CFO", "President of Finance", "Vice-President of Finance", "Senior Finance Officer", "Senior Finance Manager", "Finance Manager", "Lead Finance Associate", "Finance Associate"]
  it = ["CTO", "President of Information Technology", "Vice-President of Information Technology", "Senior Information Technology Officer", "Senior Information Technology Manager", "Information Technology Manager", "Lead Information Technology Associate", "Information Technology Associate"]
  marketing = ["President of Marketing", "Vice-President of Marketing", "Senior Marketing Officer", "Senior Marketing Manager", "Marketing Manager", "Lead Marketing Associate", "Marketing Associate"]
  operations = ["COO", "President of Operations", "Vice-President of Operations", "Senior Operations Officer", "Senior Operations Manager", "Operations Manager", "Lead Operations Associate", "Operations Associate"]
  hr = ["President of Human Resources", "Vice-President of Human Resources", "Senior Human Resources Officer", "Senior Human Resources Manager", "Human Resources Manager", "Lead Human Resources Asscociate", "Human Resources Asscociate"]

  print("Generating finance department...")
  generateFieldData(finances, CEO, 0)
  print("Generating IT department...")
  generateFieldData(it, CEO, 0)
  print("Generating Marketing department...")
  generateFieldData(marketing, CEO, 0)
  print("Generating Operations department...")
  generateFieldData(operations, CEO, 0)
  print("Generating HR department...")
  generateFieldData(hr, CEO, 0)

def generateFieldData(positions, supervisor, depth):

  if not positions:
    return

  title = positions[0]

  if depth > 2 and len(positions) > 1:
    for _ in range(random.randrange(3, 5)):
      generateEmployee(title, supervisor)
      employee = {}
      employee["name"] = completeTable["people"][-1]["address"]["nameCode"]
      employee["positionTitle"] = title
      generateFieldData(positions[1:], employee, depth+1)

  else:
    generateEmployee(title, supervisor)
    employee = {}
    employee["name"] = completeTable["people"][-1]["address"]["nameCode"]
    employee["positionTitle"] = title
    generateFieldData(positions[1:], employee, depth+1)

  return

def generateEmployee(title, supervisor):
  newPerson = createPerson()
  newAddress = createAddress(newPerson)
  newPerson["address"] = newAddress
  newWorker = createWorker(newPerson, title, supervisor)
  newPerson["address"].pop("county")
  newJobRequistion = createJobRequisition()
  newJobApplicant = createJobApplicant(newPerson)

  completeTable["addresses"].append(newAddress)
  completeTable["people"].append(newPerson)
  completeTable["workers"].append(newWorker)
  completeTable["jobRequisitions"].append(newJobRequistion)
  completeTable["jobApplicants"].append(newJobApplicant)


if __name__ == "__main__":
    main()