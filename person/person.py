import datetime
import random
from util.generateBiased import generateBiased
import pandas as pd

# @func   createPerson
# @desc   Creates person, calls other functions to generate data
# @param  None
#
def createPerson():
  person = {}

  person["gender"]                = newGender()
  person["name"]                  = newName(person)
  person["highestEducationLevel"] = newEducationLevel([100/7 for _ in range(7)])
  person["birthDate"]             = newBirthDate([100/6 for _ in range(6)])
  person["genderCode"]            = newGender()
  person["ethnicity"]             = newEthnicity([20 for _ in range(6)])

  # Address done in hcm.py file
  
  return person


#
# @func   newGender
# @desc   Creates gender
# @param  None
#
def newGender():
  MALE = 'M'
  FEMALE = 'F'
  OTHER = 'Other'

  GENDERS = [MALE, FEMALE, OTHER]

  index = random.randint(0, len(GENDERS)-1)
  gender = GENDERS[index]
  return gender


#
# @func   newName
# @desc   Creates name
# @param  Person
#
def newName(Person):
  MALE = 'M'
  FEMALE = 'F'
  middle_initials = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                  'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  male_names = pd.read_csv('assets/names/m_names.txt')['name']
  female_names = pd.read_csv('assets/names/f_names.txt')['name']
  surnames = pd.read_csv('assets/names/surnames.txt')['name']

  # index for random name out of first 100000
  name_index = random.randint(0, 100000)
  # index for random initial out of the alphabet
  initial_index = random.randint(0, 25)

  names = {}

  if Person['gender'] == MALE:
      names['firstName'] = male_names[name_index]
  elif Person['gender'] == FEMALE:
      names['firstName'] = female_names[name_index]
  else:
      names['firstName'] = male_names[name_index] if name_index % 2 == 0 else female_names[name_index]

  names['lastName'] = surnames[name_index].lower().capitalize()
  names['middleName'] = middle_initials[initial_index]

  return names


#
# @func   newEthnicity
# @desc   Creates ethnicity
# @param  percentages (weights to each race)
#
def newEthnicity(percentages):
  ETHNICITY_CODES = [
    'Non-Hispanic/Latino White',
    'Pacific Islander',
    'Native American',
    'Asian (Non-Hispanic/Latino)',
    'Non-white Hispanic/Latino',
    'African or African American (Non-Hispanic/Latino)'
  ]
  ethnicity = generateBiased(ETHNICITY_CODES, percentages)
  return ethnicity


#
# @func   newBirthDate
# @desc   Gives a random birthday.
# @param  percentages (weights to each age range)
#
def newBirthDate(percentages):
  AGE_RANGES = [20, 30, 40, 50, 60, 70]

  lowerBound = generateBiased(AGE_RANGES, percentages)
  upperBound = lowerBound + 10
  age = random.randint(lowerBound, upperBound)

  year = datetime.datetime.now().year - age
  start_dt = datetime.datetime.today().replace(year=year, day=1, month=1).toordinal()
  end_dt = datetime.datetime.today().toordinal()
  random_day = datetime.datetime.fromordinal(random.randint(start_dt, end_dt)).replace(year=year)

  return random_day


#
# @func   newEducationLevel
# @desc   Gives a random highest education level.
# @param  percentages (weights to each education level)
#
def newEducationLevel(percentages):
  educationLevels = ["High School", "GRE", "Some post-secondary education",
                  "Associate's", "Bachelor's", "Master's", "PHD"]
  highestLevelEducation = generateBiased(educationLevels, percentages)
  return highestLevelEducation


#
# @func   newEmail
# @desc   Gives a random email.
# @param  Person
#
def newEmail(Person):
  DOMAINS = ['@gmail.com', '@hotmail.com', '@aol.com', '@rjreliance.com']
  index = random.randint(0, len(DOMAINS)-1)
  Person['email'] = Person['name'] + DOMAINS[index]
  return Person


# @func   newEmployeeId
# @desc   Creates employee ID
# @param  string firstName, string lastName
#
def newEmployeeId(firstName, lastName):
  ## to do make sure employee ID is unique
  employeeId = firstName[0] + lastName

  return employeeId


# @func   newDateApplied
# @desc   Create application date
# @param  None
#
def newDateApplied():

  year = random.randrange(1990, 2019)
  month = random.randrange(1, 12)

  thirty = [4, 6, 9, 11]

  if month in thirty:
    day = random.randrange(1, 30)
  elif month == 2:
    day = random.randrange(1, 28) if not year % 4 else random.randrange(1, 29)
  else:
    day = random.randrange(1, 31)

  newDate = datetime.datetime(year, month, day)

  return newDate