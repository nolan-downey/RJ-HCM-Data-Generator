#This is a test file for the location Function Returns a list with a random location (State, City, Zip Code)

#Take a look at the States folder to get a better understanding of how this function works by looking at the text files!
#Essentially the states folder contains 50 text files 1.txt all the way to 50.txt. 
#On the first row of the text file is the state name, followed by information of cities and zip codes in that state

#Creating the empty list to return at the end of function

location = ["","",""]

#Grabbing a random integer 1-50 which corresponds to a state

from random import randint

x = str(randint(1,50))

#Concatanating the random integer to match the file path where the data is located. The data should be located in the States folder in your working directory

x = "States/" + x + '.txt'

#Reading in the data. 

with open('States/1.txt', 'r') as f: 
    file_data = f.readlines()

#Each line of the file we read into should correspond to an element in the list file_data

#Removing new line characters and accidental whitespace

file_data = [z.strip() for z in file_data]

#Getting the State put into the empty list and then deleting the first line of the file_data that contained the state name

location[0] = file_data[0]

del file_data[0]

#Now the file data list only contains elements consisting of "City,Zip_Code". 

#Using the length of the list, lets find a random integer to choose one of these elements

y = randint(0, len(file_data)-1)

#Store it in a the same list reducing its length to one 

file_data = [file_data[y]]

#Splitting the first element into two

file_data = file_data[0].split(',')

#Adding the city and zipcode to our location list

location[1] = file_data[0]
location[2] = file_data[1]

#Closing the read in variable and returning the location list

f.close()

return location
