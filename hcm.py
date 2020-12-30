#!/usr/bin/env python3

import pymongo
import ssl

from address import createAddress 
from person import createPerson
from worker import createWorker 
from jobApplicant import createJobApplicant 
from jobRequisition import createJobRequisition 

def main():
  # Eventually, we'll want to worry about user input and size of the data
  # For now, lets create the ability to randomly generate ten people

  client = pymongo.MongoClient("mongodb+srv://relianceAdmin:rjr1234!@cluster0.lx0nm.mongodb.net/hcm?retryWrites=true&w=majority", ssl_cert_reqs=ssl.CERT_NONE)
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