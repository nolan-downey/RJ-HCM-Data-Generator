import json
from random import randint
from datetime import date
import sys
from util.generateBiased import generateBiased
from jobApplicant.PreviousEmployer import createNewPreviousEmployer

CERTS = open('assets/certs.txt', 'r').readlines() 

#
# @func   createJobApplicant
# @desc   Creates job applicant, calls other functions to generate data
# @param  None
#
def createJobApplicant(Person):
  jobApplicant = {}
  jobApplicant['person'] = Person
  jobApplicant['certifications'] = newCertifications()
  jobApplicant['languages'] = newLanguages()
  jobApplicant['previousEmployer'] = createNewPreviousEmployer(jobApplicant)
  jobApplicant['ethnicityCode'] = Person['ethnicityCode']
  jobApplicant['internalApplicantIndicator'] = newInternalApplicantIndicator()
  jobApplicant['workAuthorizationIndicator'] = newWorkAuthIndicator()
  return jobApplicant

#
# @func   newInternalApplicantIndicator
# @desc   Generates new internal applicant indicator
# @param  None
#
def newInternalApplicantIndicator():
  isInternalApplicant = generateBiased([0, 1], [75, 25])
  return isInternalApplicant

#
# @func   newWorkAuthIndicator
# @desc   Generates new work authorization indicator
# @param  None
#
def newWorkAuthIndicator():
  isWorkAuthorized = generateBiased([0, 1], [10, 90])
  return isWorkAuthorized

#
# @func   newCertifications
# @desc   Creates a list of dictionaries representing the details of a person's certifications
# @param  None
#
def newCertifications():

    #Finding how many certs they have

    total_certs = generateBiased([0,1,2,3,4,5],[25,25,20,10,10,10])

    if not total_certs:
        return

    certs_data = [z.strip() for z in CERTS]

    #Need Current Date
    today = date.today()
    c_month = today.strftime('%m')
    c_year = today.strftime('%y')

    x = []

    for _ in range(total_certs):
        
        cert = certs_data[randint(0,len(certs_data)-1)]
        e_month = int(c_month) - randint(0,11)

        if(e_month <= 0):
            e_month += 12

        e_year = int(c_year) - randint(0,9)

        x.append({"Name":cert, "Effective Date": str(e_month) + "/20" + str(e_year), "End Date": str(e_month) + "/20" + str(e_year + 10)})

        certs_data.pop(certs_data.index(cert))

    # y = json.dumps(x)

    return x

#
# @func   newLanguages
# @desc   Creates a list of dictionaries representing a the details of a person's known languages
# @param  None
#
def newLanguages():
  #Ten most common languages
  LANGUAGE_CODES = ["English","Spanish","Chinese","French","Tagalog","Vietnamese","Korean","German","Arabic","Russian"]
  L_Percents = [60,10,5,5,5,5,3,3,2,2]

  #Getting the total number of languages known
  possible_total = [1,2,3,4,5]

  f_total = generateBiased(possible_total, [70,15,10,3,2])

  #If they know only one, it has to be English
  if(f_total == 1):
      x = [{"Name":"English","Native":1,"Proficiency":5}]
      # y = json.dumps(x)
      return(x)

  #Iterating through to create the languages. English is forced to be one of them.
  check = 0
  x = [] 

  for i in range(f_total):

      language = generateBiased(LANGUAGE_CODES, L_Percents)

      j = LANGUAGE_CODES.index(language)

      if(language == "English"):
          check = 1

      if(i == 0):
          x.append({"Name":language,"Native":1,"Profiency":5})
      elif(check == 0 and i == 1):
          x.append({"Name":"English","Native":0,"Profiency":randint(4,5)})
      else:
          x.append({"Name":language,"Native":0,"Profiency":randint(1,5)})

      #This deletes one of the percentages while keeping them equal to 100
      z = L_Percents[j]

      L_Percents.pop(j)

      L_Percents[0] += z

      LANGUAGE_CODES.pop(j)

  #Turning it into a JSON
  # y = json.dumps(x)

  return(x)