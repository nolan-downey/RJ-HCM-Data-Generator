from worker.workAssignment import createWorkAssignment
from worker.workerDates import createWorkerDates
from worker.workerStatus import createWorkerStatus

#
# @func   createWorker
# @desc   Creates worker, calls other functions to generate data
# @param  person object, position title, supervisor name
#
def createWorker(person, title, supervisor):
  worker = {}

  worker["person"]        = person
  worker["workerDates"]   = {}#createWorkerDates
  worker["workerStatus"]  = {}#createWorkerStatus
  worker["workAssigment"] = createWorkAssignment(worker["person"], worker["workerStatus"], title, supervisor)

  return worker