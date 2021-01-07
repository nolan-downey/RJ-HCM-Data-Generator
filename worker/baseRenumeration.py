import random

#
# @func   baseRenumeration
# @desc   Creates baseRenumeration
# @param  None
#
def baseRenumeration(position, effectiveDate):
  baseRenumeration = {}

  positionSalaries = {'Junior Marketing Associate': (45000, 65000), 'Junior Operations Associate': (45000, 65000), 'Junior HR Associate': (45000, 65000), 'Junior IT Associate': (55000, 75000), 'Marketing Associate': (65000, 95000), 'Finance Associate': (65000, 95000), 'Operations Associate': (65000, 95000), 'HR Associate': (65000, 95000), 'IT Associate': (65000, 95000), 'Lead Marketing Associate': (90000, 130000), 'Lead Marketing Manager': (90000, 130000), 'Lead Marketing Officer': (90000, 130000), 'Lead Marketing Director': (90000, 130000), 'Lead Finance Associate': (110000, 150000), 'Lead Finance Manager': (110000, 150000), 'Lead Finance Officer': (110000, 150000), 'Lead Finance Director': (110000, 150000), 'Lead Operations Associate': (90000, 130000), 'Lead Operations Manager': (90000, 130000), 'Lead Operations Officer': (90000, 130000), 'Lead Operations Director': (90000, 130000), 'Lead HR Associate': (90000, 130000), 'Lead HR Manager': (90000, 130000), 'Lead HR Officer': (90000, 130000), 'Lead HR Director': (90000, 130000), 'Lead IT Associate': (110000, 150000), 'Lead IT Manager': (110000, 150000), 'Lead IT Officer': (110000, 150000), 'Lead IT Director': (110000, 150000), 'Senior Marketing Associate': (135000, 195000), 'Senior Marketing Manager': (135000, 195000), 'Senior Marketing Officer': (135000, 195000), 'Senior Marketing Director': (135000, 195000), 'Senior Finance Associate': (165000, 225000), 'Senior Finance Manager': (165000, 225000), 'Senior Finance Officer': (165000, 225000), 'Senior Finance Director': (165000, 225000), 'Senior Operations Associate': (135000, 195000), 'Senior Operations Manager': (135000, 195000), 'Senior Operations Officer': (135000, 195000), 'Senior Operations Director': (135000, 195000), 'Senior HR Associate': (135000, 195000), 'Senior HR Manager': (135000, 195000), 'Senior HR Officer': (135000, 195000), 'Senior HR Director': (135000, 195000), 'Senior IT Associate': (165000, 225000), 'Senior IT Manager': (165000, 225000), 'Senior IT Officer': (165000, 225000), 'Senior IT Director': (165000, 225000)}
  
  minRate, maxRate = positionSalaries[position]

  baseRenumeration["annualRateAmount"]        = random.randrange(minRate, maxRate)
  baseRenumeration["monthlyRateAmount"]       = round(random.uniform(baseRenumeration["annualRateAmount"] / 12, baseRenumeration["annualRateAmount"] / 12), 2)
  baseRenumeration["weeklyRateAmount"]        = round(random.uniform(baseRenumeration["annualRateAmount"] / 52, baseRenumeration["annualRateAmount"] / 52), 2)
  baseRenumeration["dailyRateAmount"]         = round(random.uniform(baseRenumeration["weeklyRateAmount"] / 5, baseRenumeration["weeklyRateAmount"] / 5), 2)
  baseRenumeration["hourlyRateAmount"]        = round(random.uniform(baseRenumeration["dailyRateAmount"] / 8, baseRenumeration["dailyRateAmount"] / 8), 2)
  baseRenumeration["commisionRatePercentage"] = 0
  baseRenumeration["effectiveDate"]           = effectiveDate

  return baseRenumeration