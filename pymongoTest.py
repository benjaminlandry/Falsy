import datetime
import pymongo
from pymongo import MongoClient
import pprint

import uuid
from bson import ObjectId
from uuid import UUID
## json-files ##

testSuite1 = {  
    "Tag": "AFG",   
    "ClassDefinition": "AfgOfflineLicenseTestSuites",
    "TestSuiteName": "TestSuiteAfgOpenIdOfflineLicense",
    "url": "http://142.133.174.149:8888/AfgOfflineLicenseTestSuites.TestSuiteAfgOpenIdOfflineLicense?suite&format=xml"
}
        
testCases1 = {        
    "Tag": "AFG",
    "TestCaseNumber": "0700",
    "ClassDefinition": "AfgOpenIdConnectTestCases",
    "TestCaseName": "TestCase0700SuccessAfgOpenIdConnectFeatureDisable",
    "url": "http://142.133.174.149:8888/AfgOpenIdConnectTestCases.TestCase0700SuccessAfgOpenIdConnectFeatureDisable?test&format=xml",
    "description": "This test case sets the openid connect feature flag to disable. The expected behavior is that oidc requests get rejected."
}     

testSuite2 = {  
    "Tag": "AFG",   
    "ClassDefinition": "AfgVafgMasterSmokeTestSuites",
    "TestSuiteName": "TestSuiteVafgEnafGba",
    "url": "http://142.133.174.149:8888/AfgVafgMasterSmokeTestSuites.TestSuiteVafgEnafGba"
}
        
testCases2 = {        
    "Tag": "AFG",
    "TestCaseNumber": "0104",
    "ClassDefinition": "AfgIotTestCases",
    "TestCaseName": "TestCase0104FailureAfgIotEnafAuthGetReqBsfNotReachable",
    "url": "http://142.133.174.149:8888/AfgIotTestCases.TestCase0104FailureAfgIotEnafAuthGetReqBsfNotReachable?test&format=xml",
    "description": "Verify that the IOT ENAF Can send 503 error code when BSF is not reachable"
}  


## Mongo Initialization ##



# FT = client['FT'] # create a database
# RBT1 = FT['RBT'] # create a collection

# UT = client['UT']
# RBT2 = UT['RBT']

# logs = client['logs']
# testLogs = logs['TestLogs']

## Function to post and fetch to mongo ##




def postTestsToMongo():
    client = MongoClient('172.17.0.2', 27017) # connects client with the mongoserver
    FT = client['FT'] # create a database
    RBT1 = FT['RBT'] # create a collection
    UT = client['UT']
    RBT2 = UT['RBT']

    RBT1.insert_one(testSuite1) # insert a log document 
    RBT1.insert_one(testCases1)

    RBT2.insert_one(testSuite2) 
    RBT2.insert_one(testCases2)


def fetchUrlFromMongo_Suite(database, collection, Tag, ClassDefinition, TestName):
    client = MongoClient('172.17.0.2', 27017) # connects client with the mongoserver
    db = client[database] # create/connect to a database
    col = db[collection]  # create/connect to a collection

    fetchedResults = col.find_one({"Tag": Tag, "ClassDefinition": ClassDefinition, "TestSuiteName": TestName})
    return fetchedResults

def fetchUrlFromMongo_Case(database, collection, Tag, ClassDefinition, TestName, TestCaseNumber):
    client = MongoClient('172.17.0.2', 27017) # connects client with the mongoserver
    db = client[database] # create/connect to a database
    col = db[collection]  # create/connect to a collection

    fetchedResults = col.find_one({"Tag": Tag, "ClassDefinition": ClassDefinition, "TestCaseName": TestName, "TestCaseNumber": TestCaseNumber})
    return fetchedResults    

def postTestLogsToMongo(database, collection, log):
    client = MongoClient('172.17.0.2', 27017) # connects client with the mongoserver
    db = client[database] # create/connect to a database
    col = db[collection]  # create/connect to a collection
    col.insert_one(log)  # insert log document in a collection

def fetchResultsFromOneLog(database, collection, uuid):
    client = MongoClient('172.17.0.2', 27017) # connects client with the mongoserver
    db = client[database] # create/connect to a database
    col = db[collection]  # create/connect to a collection

    fetchedResults = col.find_one({"_id": uuid})
    print(fetchedResults)
    return fetchedResults 




### main ###

#postTestsToMongo()
# FT_RBT1_testSuite1 = fetchUrlFromMongo_Suite('FT', 'RBT', 'AFG', 'AfgOfflineLicenseTestSuites', 'TestSuiteAfgOpenIdOfflineLicense')
# UT_RBT2_testSuite2 = fetchUrlFromMongo_Suite('UT', 'RBT', 'AFG', 'AfgVafgMasterSmokeTestSuites', 'TestSuiteVafgEnafGba')
# FT_RBT1_testCase1 = fetchUrlFromMongo_Case('FT', 'RBT', 'AFG', 'AfgOpenIdConnectTestCases', 'TestCase0700SuccessAfgOpenIdConnectFeatureDisable')
# UT_RBT2_testCase2 = fetchUrlFromMongo_Case('UT', 'RBT', 'AFG', 'AfgIotTestCases', 'TestCase0104FailureAfgIotEnafAuthGetReqBsfNotReachable')

# print(FT_RBT1_testSuite1['url'])
# print(UT_RBT2_testSuite2['url'])
# print(FT_RBT1_testCase1['url'])
# print(FT_RBT1_testCase1['description'])
# print(UT_RBT2_testCase2['url'])
# print(UT_RBT2_testCase2['description'])




### --extra --###


# Rocket1.insert_one(testSuite3) 
# Rocket1.insert_one(testCases3)

# Rocket2.insert_one(testSuite4) 
# Rocket2.insert_one(testCases4)


# testSuite3 = {  
#     "tag": "AFG",   
#     "ClassDefinition": "AfgAfg3MasterSmokeTestSuites",
#     "FunctionDefiniton": "TestSuiteAfg3ApLicence",
#     "url": "http://142.133.174.149:8888/AfgAfg3MasterSmokeTestSuites.TestSuiteAfg3ApLicence?suite&format=xml"
# }
        
# testCases3 = {        
#     "tag": "AFG",
#     "testCaseNumber": "0701",
#     "ClassDefinition": "AfgApTestCases",
#     "FunctionDefinition": "TestCase0701FailureAfgApAutGbaNoApLicenseAfg30",
#     "url": "http://142.133.174.149:8888/AfgApTestCases.TestCase0701FailureAfgApAutGbaNoApLicenseAfg30?test&format=xml",
#     "description": "Verify that the AP and NAF cannot perform GBA authentication without any license."
# }  

# testSuite4 = {  
#     "tag": "AFG",   
#     "ClassDefinition": "AfgAfg3MasterSmokeTestSuites",
#     "FunctionDefiniton": "TestSuiteAfg3BsfLicense",
#     "url": "http://142.133.174.149:8888/AfgAfg3MasterSmokeTestSuites.TestSuiteAfg3BsfLicense?suite&format=xml"
# }
        
# testCases4 = {        
#     "tag": "AFG",
#     "testCaseNumber": "0300",
#     "ClassDefinition": "AfgBsfTestCases",
#     "FunctionDefinition": "TestCase0300SuccessAfgBsfUc300GbaDigestFeatureDisable",
#     "url": "http://142.133.174.149:8888/AfgBsfTestCases.TestCase0300SuccessAfgBsfUc300GbaDigestFeatureDisable?test&format=xml",
#     "description": "This test case sets the GBA DIgest feature flag to disable.The expected behavior is that BSF rejects. GBA Digest requires this info to work. Note: The OpenId[?] license allows GBA traffic, so it must be disabled too."
# }     