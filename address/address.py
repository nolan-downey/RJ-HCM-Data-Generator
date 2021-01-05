from randomPercentages import generateRandomEntry
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

  for key in list(statesCities.keys()):
    

  address["stateCode"] = newStateCode(list(statesCities.keys()))
  address["cityName"], address["postalCode"] = newCityZip(statesCities[address["stateCode"]])
  address["lineOne"] = newLineOne()
  
  # address["geoCoordinate"] = newGeoCoordinate()

  person["address"] = address

  return address

#
# @func   newStateCode()
# @desc   Creates new state code
# @param  None
#
def newStateCode(states):
  state = ""

  state = generateRandomEntry(states, [2 for _ in range(50)])

  return state

#
# @func   newCityZip()
# @desc   Creates new city, zipcode
# @param  None
#
def newCityZip(cityZips):

  cityZip = generateRandomEntry(cityZips, [100 / len(cityZips) for _ in range(len(cityZips))])

  return cityZip[0], cityZip[1]

#
# @func   newLineOne()
# @desc   Creates new address line one
# @param  None
#
def newLineOne():
  lineOne = ""

  return lineOne