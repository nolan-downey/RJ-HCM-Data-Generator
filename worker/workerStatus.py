import random
import datetime
from util.generateBiased import generateBiased

#
# @func createWorkerStatus
# @desc gives each worker a work status
# @param percentages (weights to each status code)
# For now, active employees only, but built for future development
#
def createWorkerStatus(workerDates):

    workerStatus = {}

    STATUS = ["Active"]
    
    if workerDates["rehireDate"] is not None:
      effectiveDate = workerDates["rehireDate"] + datetime.timedelta(days=10)
    else:
      effectiveDate = workerDates["originalHireDate"] + datetime.timedelta(days=10)

    workerStatus['status'] = STATUS[0]
    workerStatus['effectiveDate'] = effectiveDate

    return workerStatus