from util.generateBiased import generateBiased
import random
import json

streets = open("assets/Street_Names.csv", "r").readlines()
statesCities = json.load(open('assets/statesCities.json', 'r')) 

#
# @func   createAddress
# @desc   Creates address, calls other functions to generate data
# @param  None
#
def createAddress(person):
  address = {}

  address["nameCode"] = person["name"]["firstName"] + " " + person["name"]["lastName"]
  address["countryCode"] = "USA"

  address["stateCode"] = newStateCode(list(statesCities.keys()))

  cityInfo = newCityInfo(statesCities[address["stateCode"]])

  address["cityName"]       = cityInfo["name"]
  address["postalCode"]     = cityInfo["zipcode"]
  address["county"]         = cityInfo["county"]
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

  lineIndex = random.randrange(0, 2668)
  streetNumber = random.randrange(1, 999)

  street = streets[lineIndex]
  streetName = street.split(",")

  return str(streetNumber) + " " + streetName[0]