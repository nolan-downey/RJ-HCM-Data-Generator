import datetime
import numpy as np
import pandas as pd
from random import randint
from address.address import createAddress

COMPANY_NAMES = pd.read_csv('assets/companies.txt', '\t')['name']

def createNewPreviousEmployer(applicant):
  previousEmployer = {}
  previousEmployer['name'] = newEmployerName()
  previousEmployer['address'] = createAddress(applicant['person'], None)

  startDate, endDate = newStartEndDate(applicant)

  previousEmployer['startDate'] = startDate
  previousEmployer['endDate'] = endDate

  return previousEmployer

def newEmployerName():
  idx = randint(0, len(COMPANY_NAMES)-1)
  return COMPANY_NAMES[idx]

def newStartEndDate(applicant):
  startDate = ""
  endDate = ""

  yearsExperience = np.arange(1, 16)
  idx = randint(0, len(yearsExperience)-1)

  currYear = datetime.datetime.now().year
  applicantBirthYear = applicant['person']['birthDate'].year
  age = currYear - applicantBirthYear

  if age < 31:
    yearsExperience = np.arange(1, 6)
    idx = idx - 10 if idx > 5 else idx

  upperBoundYear = currYear - 2
  startYear = upperBoundYear - yearsExperience[idx-1]

  fromDate = datetime.datetime.now().replace(year=startYear, month=1, day=1).toordinal()
  tilDate = datetime.datetime.now().replace(year=startYear, month=12, day=31).toordinal()

  startDate = datetime.datetime.fromordinal(randint(fromDate, tilDate))

  fromDate = datetime.datetime.now().replace(year=upperBoundYear, month=1, day=1).toordinal()
  tilDate = datetime.datetime.now().date().toordinal()

  endDate = datetime.datetime.fromordinal(randint(fromDate, tilDate))
  return startDate, endDate