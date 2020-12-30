from gender import MALE, FEMALE, OTHER
from random import randint
import pandas as pd

middle_initials = ['A', 'B', 'C', 'D', 'E', 'I', 'J', 'K', 'L', 'M',
                  'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
male_names = pd.read_csv('./referenceData/m_names.txt')['name']
female_names = pd.read_csv('./referenceData/f_names.txt')['name']
surnames = pd.read_csv('./referenceData/surnames.txt')['name']


def newName(person):
  # index for random name out of first 100000
  name_index = randint(0, 100000)
  # index for random initial out of the alphabet
  inital_index = randint(0, 25)

  if person['gender'] == MALE:
      person['name'] = male_names[name_index]
  elif person['gender'] == FEMALE:
      person['name'] = female_names[name_index]
  else:
      person['name'] = male_names[name_index] if name_index % 2 == 0 else female_names[name_index]

  person['surname'] = surnames[name_index]
  person['middleInitial'] = middle_initials[inital_index]

  return person