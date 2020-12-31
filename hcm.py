#!/usr/bin/env python3

import pymongo
import ssl
from decouple import config

from address.address import createAddress 
from person.person import createPerson
from worker.worker import createWorker 
from jobApplicant.jobApplicant import createJobApplicant 
from jobRequisition.jobRequisition import createJobRequisition 

def main():
  # Eventually, we'll want to worry about user input and size of the data
  # For now, lets create the ability to randomly generate ten people

  uri = "mongodb+srv://{user}:{password}@cluster0.lx0nm.mongodb.net/{db}?retryWrites=true&w=majority".format(user=config("USERNAME"),password=config("PASSWORD"),db=config("DB") )

  client = pymongo.MongoClient(uri, ssl_cert_reqs=ssl.CERT_NONE)
  db = client.hcmData

  addresses = []
  people = []
  workers = []
  jobRequisitions = []
  jobApplicants = []

  for _ in range(10):
    newAddress = createAddress()
    newPerson = createPerson()
    newWorker = createWorker()
    newJobRequistion = createJobRequisition()
    newJobApplicant = createJobApplicant()

    addresses.append(newAddress)
    people.append(newPerson)
    workers.append(newWorker)
    jobRequisitions.append(newJobRequistion)
    jobApplicants.append(newJobApplicant)

  db["address"].insert_many(addresses)
  db["person"].insert_many(people)
  db["worker"].insert_many(workers)
  db["jobRequisitions"].insert_many(jobRequisitions)
  db["jobApplicants"].insert_many(jobApplicants)

if __name__ == "__main__":
    main()