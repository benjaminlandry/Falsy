import datetime
import pymongo
from pymongo import MongoClient
import pprint

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

client = MongoClient('172.17.0.2', 27017) # connects client with the mongoserver

FT = client['FT'] # create a database
RBT1 = FT['RBT'] # create a collection
#Rocket1 = FT['Rocket']

UT = client['UT']
RBT2 = UT['RBT']
#Rocket2 = UT['Rocket']

logs = client['logs']
testLogs = logs['TestLogs']


## Function to post and fetch to mongo ##

def postTestsToMongo():
    RBT1.insert_one(testSuite1) # insert a log document 
    RBT1.insert_one(testCases1)

    RBT2.insert_one(testSuite2) 
    RBT2.insert_one(testCases2)


def fetchUrlFromMongo(collection, Tag, ClassDefinition, FunctionDefinition):
    fetchedResults = collection.find_one({"Tag": Tag, "ClassDefinition": ClassDefinition, "FunctionDefinition": FunctionDefinition})
    return fetchedResults

def postTestLogsToMongo(log):
    testLogs.insert_one(log)


### main ###

postTestsToMongo()
RBT1_testSuite1 = fetchUrlFromMongo(RBT1, 'AFG', 'AfgOfflineLicenseTestSuites', 'TestSuiteAfgOpenIdOfflineLicense')
RBT2_testSuite2 = fetchUrlFromMongo(RBT2, 'AFG', 'AfgVafgMasterSmokeTestSuites', 'TestSuiteVafgEnafGba')
RBT1_testCase1 = fetchUrlFromMongo(RBT1, 'AFG', 'AfgOpenIdConnectTestCases', 'TestCase0700SuccessAfgOpenIdConnectFeatureDisable')
RBT2_testCase2 = fetchUrlFromMongo(RBT2, 'AFG', 'AfgIotTestCases', 'TestCase0104FailureAfgIotEnafAuthGetReqBsfNotReachable')

print(RBT1_testSuite1['url'])
print(RBT2_testSuite2['url'])
print(RBT1_testCase1['url'])
print(RBT1_testCase1['description'])
print(RBT2_testCase2['url'])
print(RBT2_testCase2['description'])




### --extra --###
# print(b['url'] +'\n' + b['description'])
# print(c['url'])
# print(d['url'] +'\n' + d['description'])

# Rocket1.insert_one(testSuite3) 
# Rocket1.insert_one(testCases3)

# Rocket2.insert_one(testSuite4) 
# Rocket2.insert_one(testCases4)

# a = RBT1.find_one({"tag": "AFG", "ClassDefinition": "AfgOfflineLicenseTestSuites", "FunctionDefinition": "TestCase0700SuccessAfgOpenIdConnectFeatureDisable"}) # find a document with specific fields
# b = RBT1.find_one({"tag": "AFG", "ClassDefinition": "AfgOpenIdConnectTestCases", "FunctionDefinition": "TestCase0700SuccessAfgOpenIdConnectFeatureDisable"}) 
# c = RBT2.find_one({"tag": "AFG", "ClassDefinition": "AfgVafgMasterSmokeTestSuites", "FunctionDefinition": "TestSuiteVafgEnafGba"})
# d = RBT2.find_one({"tag": "AFG", "ClassDefinition": "AfgIotTestCases", "FunctionDefinition": "TestCase0104FailureAfgIotEnafAuthGetReqBsfNotReachable"})
# # e = Rocket1.find_one({"tag": "AFG", "ClassDefinition": "AfgAfg3MasterSmokeTestSuites", "FunctionDefinition": "TestSuiteAfg3ApLicence"})
# # f = Rocket1.find_one({"tag": "AFG", "ClassDefinition": "AfgApTestCases", "FunctionDefinition": "TestCase0701FailureAfgApAutGbaNoApLicenseAfg30"})
# # g = Rocket2.find_one({"tag": "AFG", "ClassDefinition": "AfgAfg3MasterSmokeTestSuites", "FunctionDefinition": "TestSuiteAfg3BsfLicense"})
# # h = Rocket2.find_one({"tag": "AFG", "ClassDefinition": "AfgBsfTestCases", "FunctionDefinition": "TestCase0300SuccessAfgBsfUc300GbaDigestFeatureDisable"})


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