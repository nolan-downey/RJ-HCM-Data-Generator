#!/usr/bin/env python3

#
# @func   createPerson
# @desc   Creates person, calls other functions to generate data
# @param  None
#
def createPerson():
  person = {}

  person["gender"] = newGender()
  person["ethnicity"] = newEthnicity()
  person["employeeId"] = newEmployeeId(person["firstName"], person["lastName"])

  #Location Hierachy Here
  #Calls the location function returning a list into the variable location_list. This lets me index for the dictionary. Could be a better way to do this, check later
  location_list = location()
  person["country"] = "United States"
  person["state"] = location_list[0]
  person["city"] = location_list[1]
  person["zip code"] = location_list[2]

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
# @param  None
#
def newEmployeeId(firstName, lastName):
  ## to do make sure employee ID is unique
  employeeId = firstName[0] + lastName

  return employeeId


def main():
  # Eventually, we'll want to worry about user input and size of the data
  # For now, lets create the ability to randomly generate ten people

  dataset = []

  for _ in range(10):
    newPerson = createPerson()
    dataset.append(newPerson)

  print(dataset)

if __name__ == "__main__":
    main()