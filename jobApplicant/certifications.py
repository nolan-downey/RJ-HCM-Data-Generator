import json
from random import randint
from datetime import date
import sys
sys.path.insert(0,'/mnt/c/Users/jday7/Onedrive/Desktop/RJ/HMC_Code/RJ-HCM-Data-Generator/util')
from generateBiased import generateBiased

#
# @func   certifications
# @desc   Creates a list of dictionaries representing the details of a person's certifications
# @param  None
#

def certifications():

    #Finding how many certs they have

    total_certs = generateBiased([0,1,2,3,4,5],[25,25,20,10,10,10])

    if not total_certs:
        return()

    with open('assets/certs.txt', 'r') as f: 
        certs_data = f.readlines()

    certs_data = [z.strip() for z in certs_data]

    #Need Current Date
    today = date.today()
    c_month = today.strftime('%m')
    c_year = today.strftime('%y')

    x = []

    for _ in range(total_certs):
        
        cert = certs_data[randint(0,len(certs_data)-1)]
        e_month = int(c_month) - randint(0,11)

        if(e_month <= 0):
            e_month += 12

        e_year = int(c_year) - randint(0,9)

        x.append({"Name":cert, "Effective Date": str(e_month) + "/20" + str(e_year), "End Date": str(e_month) + "/20" + str(e_year + 10)})

        certs_data.pop(certs_data.index(cert))

    y = json.dumps(x)

    return(y)