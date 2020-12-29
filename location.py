#This Function Returns a list with a random location (State, City, Zip Code)

#First, we grab a random integer 1-50 which corresponds to a state

from random import randint

x = str(randint(1,50))

#Concatanating the random integer to match the file path where the data is located. The data should be located in the States folder in your working directory

x = "States/" + x + '.txt'

#Reading in the data. 

with open(x, 'r') as f: 
    file_data = f.readlines()

#Each line of the file we read into should correspond to an element in the list file_data

#Removing new line characters and accidental whitespace

file_data = [z.strip() for z in file_data]

print(file_data)