#!/usr/bin/env python3

import datetime
import random
from pprint import pprint

#
# @func   createPerson
# @desc   Creates person, calls other functions to generate data
# @param  None
#
def createPerson():
  person = {}

  person["gender"] = newGender()
  person["ethnicity"] = newEthnicity()
  #person["employeeId"] = newEmployeeId(person["firstName"], person["lastName"])

  #Location Hierachy Here
  #Calls the location function returning a list into the variable location_list. This lets me index for the dictionary. Could be a better way to do this, check later
  location_list = location()
  person["country"] = "United States"
  person["state"] = location_list[0]
  person["city"] = location_list[1]
  person["zip code"] = location_list[2]

  # Date Section
  person["dateApplied"] = newDateApplied()
  person["dateOffered"] = person["dateApplied"] + datetime.timedelta(days=random.randrange(20, 30))
  person["dateHired"] = person["dateOffered"] + datetime.timedelta(days=random.randrange(1, 14))
  person["dateLastPromotion"] = None # if not person["promotions"] else 
  person["dateTerminated"] = None

  return person

  #
# @func   newGender
# @desc   Creates gender
# @param  None
#
def newGender():
  gender = ""

  return gender

  #
# @func   newEthnicity
# @desc   Creates ethnicity
# @param  None
#
def newEthnicity():
  ethnicity = ""

  return ethnicity

# @func   location
# @desc   Gives a randomized city, state, and zip code in a list.
# @param  none

def location():

  location = [" "," "," "]

  return location

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

  newDate = datetime.date(year, month, day)

  return newDate

def main():
  # Eventually, we'll want to worry about user input and size of the data
  # For now, lets create the ability to randomly generate ten people

  dataset = []

  for _ in range(10):
    newPerson = createPerson()
    dataset.append(newPerson)

  pprint(dataset)

if __name__ == "__main__":
    main()