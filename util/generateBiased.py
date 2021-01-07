import numpy as np
from random import random

def generateBiased(data, weights):
  tieredWeights = list(np.cumsum(weights))
  rnd = random()*tieredWeights[-1]
  for idx, weight in enumerate(tieredWeights):
    if rnd < weight:
      return data[idx]