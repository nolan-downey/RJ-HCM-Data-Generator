#from workerDates import  
from worker.workAssignment import createWorkAssignment

#
# @func   createWorker
# @desc   Creates worker, calls other functions to generate data
# @param  None
#
def createWorker(person):
  worker = {}

  worker["person"]        = person
  worker["workerDates"]   = {}
  worker["workerStatus"]  = {}
  worker["workAssigment"] = createWorkAssignment(worker["person"], worker["workerStatus"])

  return worker