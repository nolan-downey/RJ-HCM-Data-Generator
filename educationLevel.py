import numpy as np
from random import randint

educationLevels = ["High School", "GRE", "Some post-secondary education",
                  "Associate's", "Bachelor's", "Master's", "PHD"]

def newhighestEducation(percentages):
    tieredPercentages = [0] + list(np.cumsum(percentages))
    index = randint(0,100)
    for i in range(0,len(educationLevels)):
        if index < tieredPercentages[i+1] and index > tieredPercentages[i]:
            return educationLevels[i]