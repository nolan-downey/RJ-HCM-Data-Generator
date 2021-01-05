import numpy as np
from random import randint

def generateRandomEntry(possibilities, percentages):
    tieredPercentages = [0] + list(np.cumsum(percentages))
    index = randint(0,100)
    for i in range(0,len(possibilities)):
        if index < tieredPercentages[i+1] and index > tieredPercentages[i] or index == tieredPercentages[i+1]:
            return possibilities[i]