import datetime
import pymongo
from pymongo import MongoClient
import pprint

# index = 9

# log = {                      # a json document
#         "tag": "AFG",
#         "suiteNumber": index,
#         "testSuiteName": "AfgOfflineLicenseTestSuites",
#         "subtestSuitename": "TestSuiteAfgOpenIdOfflineLicense"
#         }


def postToMongo(log):

    client = MongoClient('172.17.0.2', 27017) # connects client with the mongoserver
    FT = client['FT'] # create a database
    RBT = FT['RBT'] # create a collection

    logResult = RBT.insert_one(log) # insert a log document 
    pprint.pprint(RBT.find({"suiteNumber": 8}))

    client.close()

def fetchFromMongo():

    client = MongoClient('172.17.0.2', 27017) # connects client with the mongoserver
    FT = client['FT'] # create a database
    RBT = FT['RBT'] # create a collection

    return RBT.find_one({"testResults": 1})

   