import datetime
import random
import sys
sys.path.insert(0,"/mnt/c/Users/Nolan Downey/Desktop/RJReliance/RJ-HCM-Data-Generator/")
from person import person


#
# @func createWorkerDates
# @desc Combines all essential dates into one object
# @param None
#
def createWorkerDates():

  workerDates = {}
  workerDates["originalHireDate"] = createOriginalHireDate(person)
  workerDates["rehireDate"] = createRehireDate(originalHireDate)

  return workerDates

#
# @func createOriginalHireDate
# @desc Creates originalHireDate for each worker
# @param Person JSON Object, array of percentages
#
def createOriginalHireDate(person, percentages):
    
  startDt = person.birthDate + datetime.timedelta(weeks=1040)
  endDt = datetime.datetime.now()
  originalHireDate = datetime.datetime.fromordinal(random.randint(startDt, endDt))

  return originalHireDate

#
# @func createRehireDate
# @desc Creates rehire date for some of the workers
# @param originalHireDate, array of percentages
#
def createRehireDate(originalHireDate):
  
  startDt = originalHireDate
  endDt = datetime.datetime.now()
  rehireDate = datetime.datetime.fromordinal(random.randint(startDt,endDt))

  return randomDate