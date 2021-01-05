from util.generateBiased import generateBiased

ETHNICITY_CODES = [
  'Non-Hispanic/Latino White',
  'Pacific Islander',
  'Native American',
  'Asian (Non-Hispanic/Latino)',
  'Non-white Hispanic/Latino',
  'African or African American (Non-Hispanic/Latino)'
]


def newEthnicityCode(percentages):
  return generateBiased(ETHNICITY_CODES, percentages)