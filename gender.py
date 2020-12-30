from random import randint

MALE = 'M'
FEMALE = 'F'
OTHER = 'Other'

GENDERS = [MALE, FEMALE, OTHER]


def newGender():
    index = randint(0, len(GENDERS)-1)
    return GENDERS[index]
