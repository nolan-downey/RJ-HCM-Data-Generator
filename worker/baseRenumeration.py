import random

#
# @func   baseRenumeration
# @desc   Creates baseRenumeration
# @param  None
#
def baseRenumeration(position, effectiveDate):
  baseRenumeration = {}

  positionSalaries = {'Finance Associate': (55000, 75000), 'Lead Finance Associate': (65000, 85000), 'Finance Manager': (83284, 103284), 'Senior Finance Manager': (106962, 126962), 'Senior Finance Officer': (135000, 155000), 'Vice-President of Finance': (166803, 186803), 'President of Finance': (201969, 221969), 'CFO': (240203, 260203), 'Information Technology Associate': (55000, 75000), 'Lead Information Technology Associate': (65000, 85000), 'Information Technology Manager': (83284, 103284), 'Senior Information Technology Manager': (106962, 126962), 'Senior Information Technology Officer': (135000, 155000), 'Vice-President of Information Technology': (166803, 186803), 'President of Information Technology': (201969, 221969), 'CTO': (240203, 260203), 'Marketing Associate': (50000, 65000), 'Lead Marketing Associate': (60000, 75000), 'Marketing Manager': (78284, 93284), 'Senior Marketing Manager': (101962, 116962), 'Senior Marketing Officer': (130000, 145000), 'Vice-President of Marketing': (161803, 176803), 'President of Marketing': (196969, 211969), 'Operations Associate': (50000, 65000), 'Lead Operations Associate': (60000, 75000), 'Operations Manager': (78284, 93284), 'Senior Operations Manager': (101962, 116962), 'Senior Operations Officer': (130000, 145000), 'Vice-President of Operations': (161803, 176803), 'President of Operations': (196969, 211969), 'COO': (235203, 250203), 'Human Resources Asscociate': (50000, 65000), 'Lead Human Resources Asscociate': (60000, 75000), 'Human Resources Manager': (78284, 93284), 'Senior Human Resources Manager': (101962, 116962), 'Senior Human Resources Officer': (130000, 145000), 'Vice-President of Human Resources': (161803, 176803), 'President of Human Resources': (196969, 211969), 'CEO': (220000, 300000)}
  minRate, maxRate = positionSalaries[position]

  baseRenumeration["annualRateAmount"]        = random.randrange(minRate, maxRate)
  baseRenumeration["monthlyRateAmount"]       = round(random.uniform(baseRenumeration["annualRateAmount"] / 12, baseRenumeration["annualRateAmount"] / 12), 2)
  baseRenumeration["weeklyRateAmount"]        = round(random.uniform(baseRenumeration["annualRateAmount"] / 52, baseRenumeration["annualRateAmount"] / 52), 2)
  baseRenumeration["dailyRateAmount"]         = round(random.uniform(baseRenumeration["weeklyRateAmount"] / 5, baseRenumeration["weeklyRateAmount"] / 5), 2)
  baseRenumeration["hourlyRateAmount"]        = round(random.uniform(baseRenumeration["dailyRateAmount"] / 8, baseRenumeration["dailyRateAmount"] / 8), 2)
  baseRenumeration["commisionRatePercentage"] = 0
  baseRenumeration["effectiveDate"]           = effectiveDate

  return baseRenumeration