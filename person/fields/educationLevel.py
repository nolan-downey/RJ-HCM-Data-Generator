from util.generateBiased import generateBiased

educationLevels = ["High School", "GRE", "Some post-secondary education",
                  "Associate's", "Bachelor's", "Master's", "PHD"]

def newhighestEducation(percentages):
  return generateBiased(educationLevels, percentages)