from worker.baseRenumeration import baseRenumeration
from worker.reportsTo import reportsTo
from util.generateBiased import generateBiased

#
# @func   createWorkAssignment
# @desc   Creates workAssignment, calls other functions to generate data
# @param  person
#
def createWorkAssignment(person, workerStatus):
  workAssignment = {}

  workAssignment["workAssignmentID"]            = workAssignmentID()
  workAssignment["effectiveDate"]               = {}# workerStatus["effectiveDate"]
  workAssignment["assignmentStatus"]            = {}# workerStatus["effectiveDate"]
  workAssignment["assignmentCostCenterID"]      = assignmentCostCenterID()
  workAssignment["workerTypeCode"]              = workerTypeCode()
  workAssignment["managementPositionIndicator"] = managementPositionIndicator()
  workAssignment["legalEntityID"]               = legalEntityID()
  workAssignment["jobCode"]                     = {}# requisition
  workAssignment["fullTimeEquivalenceRatio"]    = fullTimeEquivalenceRatio()
  workAssignment["locationID"]                  = {}# from where person lives?
  workAssignment["payCycleCode"]                = payCycleCode()
  workAssignment["standardPayPeriodHours"]      = standardPayPeriodHours()
  workAssignment["baseRemuneration"]            = baseRenumeration(workAssignment["workerTypeCode"], workAssignment["effectiveDate"])
  workAssignment["reportsTo"]                   = reportsTo()
  workAssignment["payrollGroupCode"]            = payrollGroupCode()

  print(workAssignment)

  return workAssignment       

#
# @func   workAssigmentID
# @desc   Creates workAssignmentID
# @param  None
#
def workAssignmentID():
  workAssignment = ""

  return workAssignment

#
# @func   assignmentCostCenterID
# @desc   Creates assignmentCostCenterID
# @param  None
#
def assignmentCostCenterID():
  assignmentCostCenterID = ""

  return assignmentCostCenterID

#
# @func   workerTypeCode
# @desc   Creates workerTypeCode
# @param  None
#
def workerTypeCode():
  workerTypeCode = ""

  positions = ['Junior Marketing Associate', 'Junior Operations Associate', 'Junior HR Associate', 'Junior IT Associate', 'Marketing Associate', 'Finance Associate', 'Operations Associate', 'HR Associate', 'IT Associate', 'Lead Marketing Associate', 'Lead Marketing Manager', 'Lead Marketing Officer', 'Lead Marketing Director', 'Lead Finance Associate', 'Lead Finance Manager', 'Lead Finance Officer', 'Lead Finance Director', 'Lead Operations Associate', 'Lead Operations Manager', 'Lead Operations Officer', 'Lead Operations Director', 'Lead HR Associate', 'Lead HR Manager', 'Lead HR Officer', 'Lead HR Director', 'Lead IT Associate', 'Lead IT Manager', 'Lead IT Officer', 'Lead IT Director', 'Senior Marketing Associate', 'Senior Marketing Manager', 'Senior Marketing Officer', 'Senior Marketing Director', 'Senior Finance Associate', 'Senior Finance Manager', 'Senior Finance Officer', 'Senior Finance Director', 'Senior Operations Associate', 'Senior Operations Manager', 'Senior Operations Officer', 'Senior Operations Director', 'Senior HR Associate', 'Senior HR Manager', 'Senior HR Officer', 'Senior HR Director', 'Senior IT Associate', 'Senior IT Manager', 'Senior IT Officer', 'Senior IT Director']
  percentages = [.5, .5, .5, .5, .5, 5, 5, 5, 5, 5, .4, .4, .4, .4, .4, .4, .4, .4, .4, .4, .4, .4, .4, .4, .4, .4, .4, .4, .4, .4, .4, .4, .4, .4, .4, .4, .4, .4, .4]

  workerTypeCode = generateBiased(positions, percentages)

  return workerTypeCode

#
# @func   managementPositionIndicator
# @desc   Creates managementPositionIndicator
# @param  None
#
def managementPositionIndicator():
  managementPositionIndicator = ""

  return managementPositionIndicator

#
# @func   legalEntityID
# @desc   Creates legalEntityID
# @param  None
#
def legalEntityID():
  legalEntityID = ""

  return legalEntityID

#
# @func   fullTimeEquivalenceRatio
# @desc   Creates fullTimeEquivalenceRatio
# @param  None
#
def fullTimeEquivalenceRatio():
  fullTimeEquivalenceRatio = ""

  return fullTimeEquivalenceRatio

#
# @func   payCycleCode
# @desc   Creates payCycleCode
# @param  None
#
def payCycleCode():
  payCycleCode = ""

  return payCycleCode

#
# @func   standardPayPeriodHours
# @desc   Creates standardPayPeriodHours
# @param  None
#
def standardPayPeriodHours():
  standardPayPeriodHours = ""

  return standardPayPeriodHours

#
# @func   payrollGroupCode
# @desc   Creates payrollGroupCode
# @param  None
#
def payrollGroupCode():
  payrollGroupCode = ""

  return payrollGroupCode
