import datetime
import numpy as np
from random import randint

def newEmployerName():
  EMPLOYER_NAMES = ['Walmarket', 'Pizza Hot', 'Nokla',
                  'Macrosoft', 'ARP', 'PWCC', 'McKansey', 'Booze Jefferson']
  idx = randint(0, len(EMPLOYER_NAMES)-1)
  return EMPLOYER_NAMES[idx]
  
def newStartEndDate(applicant):
  startDate = ""
  endDate = ""

  yearsExperience = np.arange(1, 16)
  idx = randint(0, len(yearsExperience)-1)

  currYear = datetime.datetime.now().year
  applicantBirthYear = datetime.datetime.strptime(applicant['person']['birthDate'], '%Y-%b-%d').year
  age = currYear - applicantBirthYear
  
  if age < 31:
    yearsExperience = np.arange(1, 6)
    idx = idx - 10 if idx > 5 else idx

  upperBoundYear = currYear - 2
  startYear = upperBoundYear - yearsExperience[idx]

  fromDate = datetime.date().replace(year=startYear, month=1, day=1).toordinal()
  tilDate = datetime.date().replace(year=startYear, month=12, day=31).toordinal()
  
  startDate = datetime.date.fromordinal(randint(fromDate, tilDate))

  fromDate = datetime.date().replace(year=upperBoundYear, month=1, day=1).toordinal()
  tilDate = datetime.datetime.now().date().toordinal()

  endDate = datetime.date.fromordinal(randint(fromDate, tilDate))

  return startDate, endDate

def main():
  for _ in range(10):
    print(newStartEndDate({'person': {'birthDate': '2021-01-06'}}))

if __name__ == "__main__":
    main()