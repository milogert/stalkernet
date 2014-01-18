#!/usr/bin/python2

# Written by Milo Gertjejansen
# A simple program to query the MTU Stalkernet with no web scraping.

import argparse
import urllib
import json


class stalkernet:

  p = "p={0},{1},contains,{2}"
  

  def __init__(self):
    pass

  def query(self, theDict):
    aArr = buildArrayFromDict(theDict)
    return doRunQuery(aArr)
    
  def buildArrayFromDict(self, theDict):
    """Dictionary passed in must be formatted as such:

          {"category": ["operator", "query"], ...}

      The categories possible are fname, lname, fullname, email, and user.

      The operators possible are and, or, notand, and notor.
    """

    qs = []

    aAccept = ("fname", "lname", "fullname", "email", "user")

    for key, value in theDict.iteritems():
      if key in aAccept:
        print key, value
        qs.append(self.p.format(value[0], key, value[1]))

    return qs

  def doRunQuery(self, theArray):
    url = "https://www.mtu.edu/mtuldapweb/ldaprest-api/search.cgi?function=uiapi&" + "&".join(theArray)
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    return data

  def _displayData(self, theData):
    if aArgs.raw:
      print theData
    elif aArgs.all:
      for i in theData:
        for k, v in i.iteritems():
          print k + ":" + _countSpace(k) + v
        print "==============================================================================="
    elif aArgs.fields:
      for i in theData:
        for field in aArgs.fields:
          print field + ":" + _countSpace(field) + i[field]
        print "==============================================================================="
    else:
      return theData

  def _countSpace(self, theField):
    return (" " * (22 - len(theField)))


if __name__ == '__main__':
  # Start the argument parser.
  aParser = argparse.ArgumentParser(description='Query MTU StalkerNet for names of people.')
  aParser.add_argument(
    "-f",
    "--fname",
    nargs=2,
    metavar=("OPERATOR", "FIRSTNAME"),
    help="First name of person."
  )
  aParser.add_argument(
   "-l",
    "--lname",
    nargs=2,
    metavar=("OPERATOR", "LASTNAME"),
    help="Last name of person."
  )
  aParser.add_argument(
    "-a",
    "--fullname",
    nargs=2,
    metavar=("OPERATOR", "FULLNAME"),
    help="Full name of person."
  )
  aParser.add_argument(
    "-e",
    "--email",
    nargs=2,
    metavar=("OPERATOR", "EMAIL"),
    help="Email of person."
  )
  aParser.add_argument(
    "-u",
    "--user",
    nargs=2,
    metavar=("OPERATOR", "USERNAME"),
    help="Username of person."
  )

  # Argument for data viewing.
  aOutputGroup = aParser.add_mutually_exclusive_group()
  aOutputGroup.add_argument(
    "--raw",
    help="View the data as a Python dictionary. Useful for passing into other applications as JSON.",
    action="store_true",
    default=False
  )
  aOutputGroup.add_argument(
    "--all",
    help="View all the fields in the returned data.",
    action="store_true",
    default=False
  )
  aOutputGroup.add_argument(
    "--fields",
    nargs="*",
    help="A list of fields you want to display from the returned data."
  )

  aArgs = aParser.parse_args()

  # Translate the argument parser into a dictionary.
  aArgsDict = vars(aArgs)

  # Clean up the empty keys in the dictionary.
  empty_keys = [k for k,v in aArgsDict.iteritems() if not v]
  for k in empty_keys:
    del aArgsDict[k]

  # Check to see if no arguments got passed in.
  if not (aArgs.fname or aArgs.lname or aArgs.fullname or aArgs.email or aArgs.user):
    aParser.error("No action was defined. Use ./stalkernet.py -h for help")

  aNet = stalkernet()
  aArr = aNet.buildArrayFromDict(aArgsDict)
  aData = aNet.doRunQuery(aArr)
  aNet._displayData(aData)

