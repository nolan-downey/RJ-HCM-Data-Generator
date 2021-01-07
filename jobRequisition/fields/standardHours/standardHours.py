from random import randint
import numpy as np

def standardHours():
    standardHours = {}

    standardHours["fullTimeEquivalency"] = newFullTimeEquivalency()
    standardHours["dailyHoursQuantity"] = dailyHoursQuantity(standardHours)
    standardHours["weeklyHoursQuantity"] = weeklyHoursQuantity(standardHours)
    standardHours["payPeriodHoursQuantity"] = payPeriodHoursQuantity(standardHours)
    standardHours["monthlyHoursQuantity"] = monthlyHoursQuantity(standardHours)
    standardHours["annualHoursQuantity"] = annualHoursQuantity(standardHours)
    return standardHours

def newFullTimeEquivalency():
    fullTime = randint(0,1)
    # 0 = false 1 = true
    return fullTime

def dailyHoursQuantity(standardHours):
    if standardHours["fullTimeEquivalency"] == 1:
        x = np.random.normal(8,1,1)     
        dailyHoursQuantity = round(x[0])
        # 1 point with mean 8 and cov 2
    elif standardHours["fullTimeEquivalency"] == 0:
        x = np.random.normal(4,1,1)
        dailyHoursQuantity = round(x[0])
    return dailyHoursQuantity


def weeklyHoursQuantity(standardHours):
    if standardHours["fullTimeEquivalency"] == 1:
        x = np.random.normal(40,2,1)   
        weeklyHoursQuantity = round(x[0])  
        # 1 point with mean 8 and cov 2
    elif standardHours["fullTimeEquivalency"] == 0:
        x = np.random.normal(20,2,1)
        weeklyHoursQuantity = round(x[0])
    return weeklyHoursQuantity

def payPeriodHoursQuantity(standardHours):
    if standardHours["fullTimeEquivalency"] == 1:
        x = np.random.normal(80,2,1)   
        payPeriodHoursQuantity = round(x[0])  
        # 1 point with mean 8 and cov 2
    elif standardHours["fullTimeEquivalency"] == 0:
        x = np.random.normal(40,2,1)
        payPeriodHoursQuantity = round(x[0])
    return payPeriodHoursQuantity

def monthlyHoursQuantity(standardHours):
    if standardHours["fullTimeEquivalency"] == 1:
        x = np.random.normal(165,5,1)   
        monthlyHoursQuantity = round(x[0])  
        # 1 point with mean 8 and cov 2
    elif standardHours["fullTimeEquivalency"] == 0:
        x = np.random.normal(82,5,1)
        monthlyHoursQuantity = round(x[0])
    return monthlyHoursQuantity

def annualHoursQuantity(standardHours):
    if standardHours["fullTimeEquivalency"] == 1:
        x = np.random.normal(2000,20,1)   
        annualHoursQuantity = round(x[0])  
        # 1 point with mean 8 and cov 2
    elif standardHours["fullTimeEquivalency"] == 0:
        x = np.random.normal(1000,20,1)
        annualHoursQuantity = round(x[0])
    return annualHoursQuantity

def main():
    standardHours1 = standardHours()
    print(f'{standardHours1["fullTimeEquivalency"]}')
    print(f'{standardHours1["dailyHoursQuantity"]}')
    print(f'{standardHours1["weeklyHoursQuantity"]}')
    print(f'{standardHours1["monthlyHoursQuantity"]}')
    print(f'{standardHours1["annualHoursQuantity"]}')
if __name__ == "__main__":
    main()