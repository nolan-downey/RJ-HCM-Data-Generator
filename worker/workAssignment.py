import random
from worker.baseRenumeration import baseRenumeration
from util.generateBiased import generateBiased

alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                  'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#
# @func   createWorkAssignment
# @desc   Creates workAssignment, calls other functions to generate data
# @param  person
#
def createWorkAssignment(person, workerStatus, title, supervisor):
  workAssignment = {}

  workAssignment["workAssignmentID"]            = title
  workAssignment["effectiveDate"]               = {}#workerStatus["effectiveDate"]
  workAssignment["assignmentStatus"]            = {}#workerStatus["assignmentStatus"]
  workAssignment["assignmentCostCenterID"]      = None
  workAssignment["workerTypeCode"]              = workerTypeCode()
  workAssignment["managementPositionIndicator"] = managementPositionIndicator(workAssignment["workAssignmentID"].split()[-1])
  workAssignment["legalEntityID"]               = None # Organization title?
  workAssignment["fullTimeEquivalenceRatio"]    = fullTimeEquivalenceRatio()
  workAssignment["locationID"]                  = location(person["address"])
  workAssignment["payCycleCode"]                = payCycleCode()
  workAssignment["standardPayPeriodHours"]      = standardPayPeriodHours()
  workAssignment["baseRemuneration"]            = 50000 # baseRenumeration(title, workAssignment["effectiveDate"])
  workAssignment["reportsTo"]                   = supervisor
  workAssignment["payrollGroupCode"]            = payrollGroupCode()

  return workAssignment       

#
# @func   workerTypeCode
# @desc   Creates workerTypeCode
# @param  None
#
def workerTypeCode():
  types = ["employee", "contractor", "temporary"]
  percentages = [100, 0, 0]

  workerTypeCode = generateBiased(types, percentages)

  return workerTypeCode

#
# @func   managementPositionIndicator
# @desc   Creates managementPositionIndicator
# @param  position
#
def managementPositionIndicator(position):
  return True if position == "Director" or position == "Officer" or position == "Manager" else False

#
# @func   fullTimeEquivalenceRatio
# @desc   Creates fullTimeEquivalenceRatio
# @param  None
#
def fullTimeEquivalenceRatio():
  return 2080

#
# @func   location
# @desc   Creates location from address data
# @param  address
#
def location(address):
  location = {}

  location["country"] = address["countryCode"]
  location["state"]   = address["stateCode"]
  location["county"]  = address["county"]
  location["city"]    = address["cityName"]

  return location

#
# @func   payCycleCode
# @desc   Creates payCycleCode
# @param  None
#
def payCycleCode():
  return alph[random.randrange(0, 25)] + "x" + str(random.randrange(100, 10000)) + alph[random.randrange(0, 25)]

#
# @func   standardPayPeriodHours
# @desc   Creates standardPayPeriodHours
# @param  None
#
def standardPayPeriodHours():
  return 80

#
# @func   payrollGroupCode
# @desc   Creates payrollGroupCode
# @param  None
#
def payrollGroupCode():
  return alph[random.randrange(0, 25)]+ "y" + str(random.randrange(1, 100)) + alph[random.randrange(0, 25)] + str(random.randrange(1, 100))