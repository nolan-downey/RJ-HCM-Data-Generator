from worker.workAssignment import createWorkAssignment
# from worker.workerDates import createWorkerDates
# from worker.workerStatus import createWorkerStatus

#
# @func   createWorker
# @desc   Creates worker, calls other functions to generate data
# @param  None
#
def createWorker(person):
  worker = {}

  worker["person"]        = person
  worker["workerDates"]   = workerDates
  worker["workerStatus"]  = workerStatus
  worker["workAssigment"] = createWorkAssignment(worker["person"], worker["workerStatus"])

  return worker