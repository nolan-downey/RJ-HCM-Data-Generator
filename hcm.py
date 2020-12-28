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