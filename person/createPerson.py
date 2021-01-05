import datetime
import random
from person import fields

# @func   createPerson
# @desc   Creates person, calls other functions to generate data
# @param  None
#
def createPerson():
  person = {}

  person["gender"]                = fields.newGender()
  person["name"]                  = fields.newName(person)
  person["highestEducationLevel"] = fields.newEducationLevel([100/7 for _ in range(7)])
  person["birthDate"]             = fields.newBirthDate([100/12 for _ in range(12)])
  person["genderCode"]            = fields.newGender()
  person["ethnicity"]             = fields.newEthnicity([20 for _ in range(6)])

  # Address done in hcm.py file
  
  return person