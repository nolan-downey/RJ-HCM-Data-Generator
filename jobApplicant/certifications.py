#Using the file certs.csv, this file returns a list of dictionaries with the name of the certification, its effective date and end date.
#Alex gave us a lot of freedom here. He gave us a list of certs to use, but no dates. So we're assuming each cert last ten years. I also chose to not really spike this data.

import json
from random import randint
from datetime import date
import sys
sys.path.insert(0,'/mnt/c/Users/jday7/Onedrive/Desktop/RJ/HMC_Code/RJ-HCM-Data-Generator/util')

from generateBiased import generateBiased

def certifications():

    #Finding how many certs they have

    total_certs = generateBiased([0,1,2,3,4,5],[25,25,20,10,10,10])


    if(total_certs == 0):
        return(0)

    with open('assets/certs.txt', 'r') as f: 
        certs_data = f.readlines()
    f.close()

    certs_data = [z.strip() for z in certs_data]

    #Need Current Date
    today = date.today()
    c_month = today.strftime('%m')
    c_year = today.strftime('%y')

    i = 0
    x = [""] * total_certs

    while(i < total_certs):

        cert = certs_data[randint(0,len(certs_data)-1)]
        e_month = int(c_month) - randint(0,11)

        if(e_month <= 0):
            e_month += 12

        e_year = int(c_year) - randint(0,9)

        x[i] = {"Name":cert, "Effective Date": str(e_month) + "/20" + str(e_year), "End Date": str(e_month) + "/20" + str(e_year + 10)}

        del certs_data[certs_data.index(cert)]
        i += 1

    y = json.dumps(x)

    return(y)