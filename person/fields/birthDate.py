from random import randint
import datetime
import calendar
import numpy as np

AGE_RANGES = [20, 30, 40, 50, 60, 70]

def newBirthDate(percentages):
  age = 0
  tieredPercentages = [0] + list(np.cumsum(percentages))
  index = randint(0, 100)
  for i in range(0, len(AGE_RANGES)-1):
    if index <= tieredPercentages[i+1] and index >= tieredPercentages[i]:
      age = randint(AGE_RANGES[i], AGE_RANGES[i+1])

  year = datetime.datetime.now().year - age
  start_dt = datetime.date.today().replace(year=year, day=1, month=1).toordinal()
  end_dt = datetime.date.today().toordinal()
  random_day = datetime.date.fromordinal(randint(start_dt, end_dt)).replace(year=year)

  return random_day