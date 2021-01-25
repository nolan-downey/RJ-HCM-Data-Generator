from worker.workAssignment import createWorkAssignment
from worker.workerDates import createWorkerDates
from worker.workerStatus import createWorkerStatus

#
# @func   createWorker
# @desc   Creates worker, calls other functions to generate data
# @param  person object, position title, supervisor name
#
def createWorker(person, title, supervisor, depth, probabilities):
  worker = {}

  worker["person"]          = person
  worker["workerDates"]     = createWorkerDates(person)
  worker["workerStatus"]    = createWorkerStatus(worker["workerDates"])
  worker["workAssignment"]  = createWorkAssignment(worker["person"], worker["workerStatus"], title, supervisor, depth, probabilities)

  return worker