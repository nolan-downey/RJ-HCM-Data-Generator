from random import randint

EMPLOYER_NAMES = ['Walmarket', 'Pizza Hot', 'Nokla',
                  'Macrosoft', 'ARP', 'PWCC', 'McKansey', 'Booze Jefferson']

def newEmployerName():
  index = randint(0, len(EMPLOYER_NAMES)-1)
  return EMPLOYER_NAMES[index]