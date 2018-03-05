import datetime
import pymongo
from pymongo import MongoClient

import uuid
from bson import ObjectId
from uuid import UUID
import json
import os
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
    "url": "http://142.133.174.149:8888/AfgVafgMasterSmokeTestSuites.TestSuiteVafgEnafGba?suite&format=xml"
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
    # FT = client['FT'] # create a database
    # RBT1 = FT['RBT'] # create a collection
    # UT = client['UT']
    # RBT2 = UT['RBT']

    logs = client['logs']
    TCM = logs['TestCatalogManager']

    TCM.insert_one(json.load(open('tcm_template.json')))
    # RBT1.insert_one(testSuite1) # insert a log document 
    # RBT1.insert_one(testCases1)

    # RBT2.insert_one(testSuite2) 
    # RBT2.insert_one(testCases2)


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

    fetchedResults = col.find_one({"_id": uuid}, {"testResults.result.tables" : 0, "testResults.result.instructions": 0, "testResults.result.content": 0})
    return fetchedResults 

def updateTCMTemplate(database, collection, uuid, log):
    client = MongoClient('172.17.0.2', 27017) # connects client with the mongoserver
    db = client[database] # create/connect to a database
    col = db[collection]  # create/connect to a collection
   # col.find_one_and_update({"_id": uuid}, {'$set': {'testcatalogmanager': {'ut': {'tests': [{'data': log}]}}}}) 
    col.find_one_and_replace({"_id": uuid}, {'testcatalogmanager': log}) #TODO: fix later, duplicate 'testcatalogmanager' name in JSON

def fetchUUID(database, collection, tag, testCatalog, target_tool, testType, testName, uuid):
    client = MongoClient('172.17.0.2', 27017) # connects client with the mongoserver
    db = client[database] # create/connect to a database
    col = db[collection]  # create/connect to a collection
    
    logDirectory = col.find_one({"testcatalogmanager.ut.tests.target_tool.type": target_tool})
    #logDirectory = col.find({['testcatalogmanager']['ut']['tests']['target_tool']['type']: target_tool})

    print(logDirectory)
    #TODO: grab UT, RBT, and name parameters to pick an '_id'
    
    # return i['_id']


### main ###
#template_uuid = fetchDocWithUUID('ebbad7ce-17ed-11e8-accf-0ed5f89f718a')
template_uuid = fetchUUID('logs', 'TestCatalogManager', 'AFG', 'ut', 'Rocket', 'ts', 'AfgOfflineLicenseTestSuites.TestSuiteAfgOpenIdOfflineLicense', 'ebbad7ce-17ed-11e8-accf-0ed5f89f718a')
#print(template_uuid)

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


