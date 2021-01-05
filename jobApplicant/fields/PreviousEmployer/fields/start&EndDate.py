import datetime

def newStartEndDate(applicant):
  age = datetime.datetime.now().year - applicant['person'].birthDate.year
  
