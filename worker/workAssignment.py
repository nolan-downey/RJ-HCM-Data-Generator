import random
from worker.baseRenumeration import baseRenumeration
from worker.reportsTo import reportsTo
from util.generateBiased import generateBiased

alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                  'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#
# @func   createWorkAssignment
# @desc   Creates workAssignment, calls other functions to generate data
# @param  person
#
def createWorkAssignment(person, workerStatus):
  workAssignment = {}

  workAssignment["workAssignmentID"]            = workAssignmentID()
  workAssignment["effectiveDate"]               = {} # workerStatus["effectiveDate"]
  workAssignment["assignmentStatus"]            = {} # workerStatus["assignmentStatus"]
  workAssignment["assignmentCostCenterID"]      = None
  workAssignment["workerTypeCode"]              = workerTypeCode()
  workAssignment["managementPositionIndicator"] = managementPositionIndicator(workAssignment["workAssignmentID"].split()[-1])
  workAssignment["legalEntityID"]               = None # Organization title?
  workAssignment["fullTimeEquivalenceRatio"]    = fullTimeEquivalenceRatio()
  workAssignment["locationID"]                  = location(person["address"])
  workAssignment["payCycleCode"]                = payCycleCode()
  workAssignment["standardPayPeriodHours"]      = standardPayPeriodHours()
  workAssignment["baseRemuneration"]            = baseRenumeration(workAssignment["workAssignmentID"], workAssignment["effectiveDate"])
  # workAssignment["reportsTo"]                   = reportsTo()
  workAssignment["payrollGroupCode"]            = payrollGroupCode()

  return workAssignment       

#
# @func   workAssigmentID
# @desc   Creates workAssignmentID
# @param  None
#
def workAssignmentID():
  positions = ['Junior Marketing Associate', 'Junior Operations Associate', 'Junior HR Associate', 'Junior IT Associate', 'Marketing Associate', 'Finance Associate', 'Operations Associate', 'HR Associate', 'IT Associate', 'Lead Marketing Associate', 'Lead Marketing Manager', 'Lead Marketing Officer', 'Lead Marketing Director', 'Lead Finance Associate', 'Lead Finance Manager', 'Lead Finance Officer', 'Lead Finance Director', 'Lead Operations Associate', 'Lead Operations Manager', 'Lead Operations Officer', 'Lead Operations Director', 'Lead HR Associate', 'Lead HR Manager', 'Lead HR Officer', 'Lead HR Director', 'Lead IT Associate', 'Lead IT Manager', 'Lead IT Officer', 'Lead IT Director', 'Senior Marketing Associate', 'Senior Marketing Manager', 'Senior Marketing Officer', 'Senior Marketing Director', 'Senior Finance Associate', 'Senior Finance Manager', 'Senior Finance Officer', 'Senior Finance Director', 'Senior Operations Associate', 'Senior Operations Manager', 'Senior Operations Officer', 'Senior Operations Director', 'Senior HR Associate', 'Senior HR Manager', 'Senior HR Officer', 'Senior HR Director', 'Senior IT Associate', 'Senior IT Manager', 'Senior IT Officer', 'Senior IT Director']
  percentages = [2.63, 2.63, 2.63, 2.63, 2.63, 10, 10, 10, 10, 10, 2.63, 2.63, 2.63, 2.63, 2.63, 2.63, 2.63, 2.63, 2.63, 2.63, 2.63, 2.63, 2.63, 2.63, 2.63, 2.63, 2.63, 2.63, 2.63, 2.63, 2.63, 2.63, 2.63, 2.63, 2.63, 2.63, 2.63, 2.63, 2.63]

  workAssignment = generateBiased(positions, percentages)

  return workAssignment

#
# @func   workerTypeCode
# @desc   Creates workerTypeCode
# @param  None
#
def workerTypeCode():
  types = ["employee", "contractor", "temporary"]
  percentages = [95, 2.5, 2.5]

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