import datetime
import random
import sys
from person import person

#
# @func createWorkerDates
# @desc Combines all essential dates into one object
# @param None
#
def createWorkerDates(person):

  workerDates = {}
  workerDates["originalHireDate"] = createOriginalHireDate(person)
  workerDates["rehireDate"] = createRehireDate(workerDates["originalHireDate"])

  return workerDates

#
# @func createOriginalHireDate
# @desc Creates originalHireDate for each worker
# @param Person JSON Object, array of percentages
#
def createOriginalHireDate(person):
    
  startDt = person["birthDate"] + datetime.timedelta(weeks=1040)
  endDt = datetime.datetime.now().toordinal()
  originalHireDate = datetime.datetime.fromordinal(random.randint(startDt.toordinal(), endDt))

  return originalHireDate

#
# @func createRehireDate
# @desc Creates rehire date for some of the workers
# @param originalHireDate, array of percentages
#
def createRehireDate(originalHireDate):
  
  chance = random.randint(0,100)
  if chance >= 15:
      return None

  startDt = originalHireDate.toordinal()
  endDt = datetime.datetime.now().toordinal()
  rehireDate = datetime.datetime.fromordinal(random.randint(startDt,endDt))
    
  return rehireDate