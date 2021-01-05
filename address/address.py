from util.generateBiased import generateBiased
import random
import json

#
# @func   createAddress
# @desc   Creates address, calls other functions to generate data
# @param  None
#
def createAddress(person):
  address = {}

  address["nameCode"] = "Robert Reutiman"
  # address["nameCode"] = person.personName.firstName + person.personName.lastName
  address["countryCode"] = "USA"

  statesCities = json.load(open('statesCities.json', 'r'))    

  address["stateCode"] = newStateCode(list(statesCities.keys()))

  cityInfo = newCityInfo(statesCities[address["stateCode"]])

  address["cityName"]       = cityInfo["name"]
  address["postalCode"]     = cityInfo["zipcode"]
  address["lineOne"]        = newLineOne()
  address["geoCoordinate"]  = {"longitude": cityInfo["longitude"], "latitude": cityInfo["latitude"]}

  person["address"] = address

  return address

#
# @func   newStateCode()
# @desc   Creates new state code
# @param  states
#
def newStateCode(states):
  return generateBiased(states, [2 for _ in range(52)])

#
# @func   newCityInfo()
# @desc   Creates new city profile
# @param  cities
#
def newCityInfo(cities):
  return generateBiased(cities, [100 / len(cities) for _ in range(len(cities))])

#
# @func   newLineOne()
# @desc   Creates new address line one
# @param  None
#
def newLineOne():

  with open("Street_Names.csv", "r") as streetFile:

    lineIndex = random.randrange(1, 2670)
    streetNumber = random.randrange(1, 999)

    streets = streetFile.readlines()
    street = streets[lineIndex]
    streetName = street.split(",")

  return str(streetNumber) + " " + streetName[0]