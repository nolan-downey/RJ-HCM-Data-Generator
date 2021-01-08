from random import randint
import json
import sys
sys.path.insert(0,'/mnt/c/Users/jday7/Onedrive/Desktop/RJ/HMC_Code/RJ-HCM-Data-Generator/util')
from generateBiased import generateBiased

#
# @func   languages
# @desc   Creates a list of dictionaries representing a the details of a person's known languages
# @param  None
#

def languages():

    #Ten most common languages
    LANGUAGE_CODES = ["English","Spanish","Chinese","French","Tagalog","Vietnamese","Korean","German","Arabic","Russian"]
    L_Percents = [60,10,5,5,5,5,3,3,2,2]

    #Getting the total number of languages known
    possible_total = [1,2,3,4,5]

    f_total = generateBiased(possible_total, [70,15,10,3,2])

    #If they know only one, it has to be English
    if(f_total == 1):
        x = [{"Name":"English","Native":1,"Proficiency":5}]
        y = json.dumps(x)
        return(y)


    #Iterating through to create the languages. English is forced to be one of them.
    check = 0
    x = [] 

    for i in range(f_total):

        language = generateBiased(LANGUAGE_CODES, L_Percents)

        j = LANGUAGE_CODES.index(language)

        if(language == "English"):
            check = 1

        if(i == 0):
            x.append({"Name":language,"Native":1,"Profiency":5})
        elif(check == 0 and i == 1):
            x.append({"Name":"English","Native":0,"Profiency":randint(4,5)})
        else:
            x.append({"Name":language,"Native":0,"Profiency":randint(1,5)})

        #This deletes one of the percentages while keeping them equal to 100
        z = L_Percents[j]

        L_Percents.pop(j)

        L_Percents[0] += z

        LANGUAGE_CODES.pop(j)


    #Turning it into a JSON
    y = json.dumps(x)

    return(y)