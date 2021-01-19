import pandas as pd
import numpy as np
import datetime
from pprint import pprint
from random import randint

from worker.worker import createWorker
from util.generateBiased import generateBiased

TITLES = pd.read_csv('assets/requisitionTitles.txt', ',\n', error_bad_lines=False)['names']
REASONS = ['New position']
TRAVEL_REQUIREMENT_PERCENTAGES = [10, 15, 20, 25, 30, 35]
MONTHS_IN_ADVANCE = [1, 2, 3, 4, 5, 6]
CONTRACT_LENGHTS = [1, 2, 3]
FILLED_QUANTITIES = np.arange(1,51)
STATUS_CODES = ['Pending', 'Approved', 'Filled', 'Closed']

#
# @func   createJobRequisition
# @desc   Creates requisition, calls other functions to generate data
# @param  None
#
def createJobRequisition(positionTitle):
  requisition = {}
  title, reason = newTitleReason()
  requisition['requisitionTitle'] = positionTitle
  requisition['requisitionReasonCode'] = reason
  requisition['positionTravelRequirement'] = newTravelRequirement()
  requisition['postDate'] = newPostDate()
  requisition['standardHours'] = {} # upon completion of standardHours
  requisition['bonusEligibleIndicator'] = newBonusEligIndicator()
  requisition['projectedStartDate'] = newProjectedStartDate()
  requisition['projectedEndDate'] = newProjectedEndDate(requisition['projectedStartDate'])
  requisition['openingsFilledQuantity'] = newOpeningsFilledQuantity()
  requisition['requisitionStatusCode'] = newStatusCode()
  requisition['filledDate'] = newFillDate(requisition['requisitionStatusCode'], 
                                          requisition['postDate'], 
                                          requisition['projectedStartDate'])
  requisition['remoteIndicator'] = newRemoteIndicator()
  requisition['requisitionLocations'] = {} # upon completion of location
  requisition['hiringManager'] = {} # need to decide how to integrate workers
  requisition['recruiter'] = {} # need to decide how to integrate workers

  return requisition


def newTitleReason():
  titleIndex = randint(0, len(TITLES)-1)
  reasonIndex = randint(0, len(REASONS)-1)
  copy = list(TITLES)
  requisitionTitle = copy.pop(titleIndex).title()
  requisitionReason = REASONS[reasonIndex]

  return requisitionTitle, requisitionReason

def newTravelRequirement():
  index = randint(0, len(TRAVEL_REQUIREMENT_PERCENTAGES)-1)
  travelRequirement = TRAVEL_REQUIREMENT_PERCENTAGES[index]
  travelRequirementStr = f"{travelRequirement}% or more"

  return travelRequirementStr

def newPostDate():
  twoYearsAgo = datetime.datetime.now().year - 2
  dateTwoYearsAgo = datetime.datetime.now().replace(year=twoYearsAgo, month=1, day=1).toordinal()
  tilDate = datetime.datetime.now().toordinal()
  postDate = datetime.datetime.fromordinal(randint(dateTwoYearsAgo, tilDate))

  return postDate

def newBonusEligIndicator():
  isBonusEligible = generateBiased([0, 1], [20, 80])
  return isBonusEligible 

def newProjectedStartDate():
  monthsInAdvance = MONTHS_IN_ADVANCE[randint(0, len(MONTHS_IN_ADVANCE)-1)]

  currDate = datetime.datetime.now()
  fromDate = currDate.replace(month=currDate.month + 1).toordinal()
  tilDate = currDate.replace(month=currDate.month + monthsInAdvance).toordinal()
  randomDay = datetime.datetime.fromordinal(randint(fromDate, tilDate))
  projectedStartDate = datetime.datetime.fromordinal(randomDay.toordinal() - randomDay.weekday()) # assuming weekly pay periods

  return projectedStartDate

def newProjectedEndDate(startDate):
  contractLength = CONTRACT_LENGHTS[randint(0, len(CONTRACT_LENGHTS)-1)]
  projectedEndDate = startDate.replace(year=startDate.year + contractLength)
  return projectedEndDate

def newOpeningsFilledQuantity():
  openingsFilledQuantity = FILLED_QUANTITIES[randint(0, len(FILLED_QUANTITIES)-1)]
  return int(openingsFilledQuantity)

def newStatusCode():
  statusCode = generateBiased(STATUS_CODES, [50, 50/3, 50/3, 50/3])
  return statusCode

def newFillDate(statusCode, postDate: datetime.datetime, projectedStartDate: datetime.datetime):
  if statusCode != 'Filled':
    return ""
  fromDate = postDate.toordinal()
  tilDate = projectedStartDate.toordinal()
  fillDate = datetime.datetime.fromordinal(randint(fromDate, tilDate))
  return fillDate

def newRemoteIndicator():
  isRemote = generateBiased([0, 1], [80, 20])
  return isRemote