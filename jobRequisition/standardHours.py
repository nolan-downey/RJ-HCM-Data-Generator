from random import randint
import numpy as np
from util.generateBiased import generateBiased

def standardHours(fullTimePercentages):
    standardHours = {}

    standardHours["fullTimeEquivalency"] = newFullTimeEquivalency(fullTimePercentages if fullTimePercentages else None)
    standardHours["dailyHoursQuantity"] = dailyHoursQuantity(standardHours["fullTimeEquivalency"])
    standardHours["weeklyHoursQuantity"] = weeklyHoursQuantity(standardHours["fullTimeEquivalency"])
    standardHours["payPeriodHoursQuantity"] = payPeriodHoursQuantity(standardHours["fullTimeEquivalency"])
    standardHours["monthlyHoursQuantity"] = monthlyHoursQuantity(standardHours["fullTimeEquivalency"])
    standardHours["annualHoursQuantity"] = annualHoursQuantity(standardHours["fullTimeEquivalency"])
    return standardHours

def newFullTimeEquivalency(fullTimePercentages):
    fullTime = generateBiased([0,1], fullTimePercentages if fullTimePercentages else [50,50])
    # 0 = false 1 = true
    return fullTime

def dailyHoursQuantity(fTE):
    if fTE:
        x = np.random.normal(8,1,1)     
        dailyHoursQuantity = round(x[0])
        # 1 point with mean 8 and cov 2
    else:
        x = np.random.normal(4,1,1)
        dailyHoursQuantity = round(x[0])
    return dailyHoursQuantity

def weeklyHoursQuantity(fTE):
    if fTE:
        x = np.random.normal(40,2,1)   
        weeklyHoursQuantity = round(x[0])  
        # 1 point with mean 8 and cov 2
    else:
        x = np.random.normal(20,2,1)
        weeklyHoursQuantity = round(x[0])
    return weeklyHoursQuantity

def payPeriodHoursQuantity(fTE):
    if fTE:
        x = np.random.normal(80,2,1)   
        payPeriodHoursQuantity = round(x[0])  
        # 1 point with mean 8 and cov 2
    else:
        x = np.random.normal(40,2,1)
        payPeriodHoursQuantity = round(x[0])
    return payPeriodHoursQuantity

def monthlyHoursQuantity(fTE):
    if fTE:
        x = np.random.normal(165,5,1)   
        monthlyHoursQuantity = round(x[0])  
        # 1 point with mean 8 and cov 2
    else:
        x = np.random.normal(82,5,1)
        monthlyHoursQuantity = round(x[0])
    return monthlyHoursQuantity

def annualHoursQuantity(fTE):
    if fTE:
        x = np.random.normal(2000,20,1)   
        annualHoursQuantity = round(x[0])  
        # 1 point with mean 8 and cov 2
    else:
        x = np.random.normal(1000,20,1)
        annualHoursQuantity = round(x[0])
    return annualHoursQuantity