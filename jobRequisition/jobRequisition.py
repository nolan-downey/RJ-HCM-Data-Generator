import pandas as pd
from datetime import datetime, date
from random import randint

REQUISITION_TITLES = pd.read_csv('assets/requisitionTitles.txt', ',\n', error_bad_lines=False)['names']
REQUISITION_REASONS = ['New position']
STATUS_CODES = ['Open', 'Closed']
TRAVEL_REQUIREMENT_PERCENTAGES = [10, 15, 20, 25, 30, 35]

#
# @func   createJobRequisition
# @desc   Creates requisition, calls other functions to generate data
# @param  None
#
def createJobRequisition():
  requisition = {}
  title, reason = newTitleReason()
  requisition['requisitionTitle'] = title
  requisition['requisitionReasonCode'] = reason
  requisition['positionTravelRequirement'] = newTravelRequirement()
  requisition['postDate'] = newPostDate()

  return requisition

def newTitleReason():
  index = randint(0, len(REQUISITION_TITLES)-1)
  requisitionTitle = REQUISITION_TITLES.pop(index)
  requisitionReason = REQUISITION_REASONS[index]
  return requisitionTitle, requisitionReason

def newTravelRequirement():
  index = randint(0, len(TRAVEL_REQUIREMENT_PERCENTAGES)-1)
  travelRequirement = TRAVEL_REQUIREMENT_PERCENTAGES[index]
  travelRequirementStr = f"{travelRequirement}% or more"
  return travelRequirementStr

def newPostDate():
  twoYearsAgo = datetime.now().year - 2
  dateTwoYearsAgo = datetime.now().replace(year=twoYearsAgo, month=1, day=1).toordinal()
  tilDate = datetime.now().toordinal

  postDate = date.fromordinal(tilDate)
  return postDate

def createStandardHours():
  pass

def newJobcode():
  pass