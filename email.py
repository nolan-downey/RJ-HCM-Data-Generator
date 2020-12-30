from random import randint
DOMAINS = ['@gmail.com', '@hotmail.com', '@aol.com', '@rjreliance.com']

def email(person):
  index = randint(0, len(DOMAINS)-1)
  person['email'] = person['name'] + DOMAINS[index]
  return person