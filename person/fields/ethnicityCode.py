import os, sys
sys.path.insert(0, os.path.abspath(".."))
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

def main():
  count = 0
  count_dict = {}
  for i in range(100000):
    eth = newEthnicityCode([0, 0.75, 29.25, 20, 25, 25])
    count_dict[eth] = count_dict.get(eth, 0) + 1
    if (eth): count += 1
  print(count)
  print(count_dict)

if __name__ == "__main__":
    main()