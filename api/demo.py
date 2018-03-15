import datetime
import pymongo
from pymongo import MongoClient

import requests
import falsy

import json
from json import dumps

import re
from lxml import etree
from bs4 import BeautifulSoup

import xmltodict
import pymongoTest 
import uuid
from uuid import UUID
from bson import ObjectId
import os

##
mongoIP=os.environ.get('MONGODB_HOST')
print('demo.py file')
print(mongoIP)
## 


def get_it_TC(TestCaseName, TestCaseNumber, Tag):
    pass
def get_it_TS(TestSuiteName, Tag):
    pass

# ^^ new ^^ #


pymongoTest.postTestsToMongo(mongoIP)
tcm_template = pymongoTest.fetchDocWithUUID(mongoIP, 'logs', 'TestCatalogManager', "ebbad7ce-17ed-11e8-accf-0ed5f89f718b") 
print(tcm_template)


# #TS

# #uuid = ObjectId("5a908064d5b67f3dd2e630ae")

# template_uuid = 'ebbad7ce-17ed-11e8-accf-0ed5f89f718bbb' #variable given in swagger-user-body
# tcm_template = pymongoTest.fetchDocWithUUID(mongoIP, 'logs', 'TestCatalogManager', 'Rocket', template_uuid)
# #print(tcm_template)

# tag = 'AFG'
# testName = 'R1A15'

# ## logic for parsing logs
# # totalResult_right = logData['testResults']['finalCounts']['right']
# # totalResult_wrong = logData['testResults']['finalCounts']['wrong']

# # if (totalResult_wrong == '0') and (totalResult_right >= 0):
# #     totalResult = 'Success'
# # else:
# #     totalResult = 'Failure'


# # for x in logData['testResults']['result']:
# #     #Test_case
# #     Test_Case = (x['relativePageName'])
# #     #Test_result
# #     result_right = (x['counts']['right'])
# #     result_wrong = (x['counts']['wrong'])

# #     if (result_wrong == '0') and (result_right >= 0):
# #         result =def get_it_TS: 'Success'
# #     else:
# #         result = 'Failure'
# #     print(result)
# #     #Time Evaluation
# #     duration = (x['runTimeInMillis'])
# #     print(duration)

# #TODO: TODELETE - testParameters
# duration = 123
# Test_Case = "abc"
# result = "Success"
# totalResult = "success"
# ##

# #JSON-body

# data_result = {
#     "Test_Case": str(Test_Case),
#     "Test_Result": str(result),
#     "Time Evaluation": str(duration)
# }
   

# res2 = tcm_template['testcatalogmanager']['ut']['tests']
# for res3 in res2:
#     res4 = res3['data']
#     for res5 in res4: # # res4 in data list     
#         final_result = res5['results']
#         final_result.append(data_result)


# for tcm2 in tcm_template['testcatalogmanager']['ut']['tests']:
#     for tcm3 in tcm2:
#         tcm3 = final_result


# data = [{
#     "uuid": str(uuid),
#     "name": str(tag + "_" + testName + "_" + str(datetime.datetime.utcnow())),
#     "verdict": str(totalResult),
#     "result": tcm3
# }]

# for tcm2b in tcm_template['testcatalogmanager']['ut']['tests']:
#     tcm2b['data'] = data

# print(tcm_template['testcatalogmanager'])

# pymongoTest.updateTCMTemplate(mongoIP, 'logs', 'TestCatalogManager', template_uuid, tcm_template['testcatalogmanager'])





# def get_it_TC(TestCaseName, TestCaseNumber, Tag):

#     ## mongo ##
    
#     fetchedCase = pymongoTest.fetchUrlFromMongo_Case(mongoIP, 'FT', 'RBT', 'AFG', 'AfgOpenIdConnectTestCases', 'TestCase0700SuccessAfgOpenIdConnectFeatureDisable', '0700')

#     # database = 'FT'
#     # collection = 'RBT'
#     # fetchedCase = pymongoTest.fetchUrlFromMongo_Suite(database, collection, Tag, ClassDefinition, TestCaseName, TestCaseNumber)
#     # print(fetchedCase['url'])

#     ## requests ##
#     r = requests.get(fetchedCase['url'])
#     data = r.text
#     #appendData = {str(uuid.uuid4())} + r.text
#     dataInJson = xmltodict.parse(data)
#     print(dataInJson)
#     #print(dataInJson)
#     ## append data
    


#     ## logs
    
#     #pymongoTest.postTestLogsToMongo(mongoIP, 'logs', 'TestLogs', dataInJson)
#     #print(str(uuid.uuid4()))
#     uuid = ObjectId("5a8ee5fdd5b67f1d6831c50a")
#     logData = pymongoTest.fetchResultsFromOneLog(mongoIP, 'logs', 'TestLogs', uuid)
#     print(logData)
#     ###
   
#     # f = open('Test_logs.xml', 'w')
#     # f.write(data)
#     # f.close()
#     # infile = open("Test_logs.xml","r")

#     # contents = infile.read()
#     # soup = BeautifulSoup(contents,'xml')
#     # hi = soup.get_text()
#     return logData


# def get_it_TS(TestSuiteName, Tag, uuid):
    
#     ## fetch test_url from TMS_template, in mongo
#     tcm_template = pymongoTest.fetchDocWithUUID(mongoIP, 'logs', 'TestLogs', "ebbad7ce-17ed-11e8-accf-0ed5f89f718b") 
#     # database = 'logs'
#     # collection = 'TestLogs'
#     #fetchedSuite = pymongoTest.fetchUrlFromMongo_Suite(mongoIP, database, collection, Tag, ClassDefinitionTestSuiteName)
#     res2 = (tcm_template['testcatalogmanager']['ut']['tests'])
#     for res3 in res2:
#         test_url = res3['url'] # check syntax
#     ##

#     ## requests to testServer
#     r = requests.get(fetchedSuite['url'])
#     data = r.text
#     dataInJson = xmltodict.parse(data)
#     print(dataInJson)
#     # post logs to mongo
#     pymongoTest.postTestLogsToMongo(mongoIP, 'logs', 'TestLogs', dataInJson) 
#     ##

#     ###


#     ## logic for parsing logs
#     # totalResult_right = logData['testResults']['finalCounts']['right']
#     # totalResult_wrong = logData['testResults']['finalCounts']['wrong']

#     # if (totalResult_wrong == '0') and (totalResult_right >= 0):
#     #     totalResult = 'Success'
#     # else:
#     #     totalResult = 'Failure'


#     # for x in logData['testResults']['result']:
#     #     #Test_case
#     #     Test_Case = (x['relativePageName'])
#     #     #Test_result
#     #     result_right = (x['counts']['right'])
#     #     result_wrong = (x['counts']['wrong'])

#     #     if (result_wrong == '0') and (result_right >= 0):
#     #         result = 'Success'
#     #     else:
#     #         result = 'Failure'
#     #     print(result)
#     #     #Time Evaluation
#     #     duration = (x['runTimeInMillis'])
#     #     print(duration)
#     ##

#     ## updating mongo document for logResults
#     data_result = {
#         "Test_Case": str(Test_Case),
#         "Test_Result": str(result),
#         "Time Evaluation": str(duration)
#     }
    

#     res2 = tcm_template['testcatalogmanager']['ut']['tests']
#     for res3 in res2:
#         res4 = res3['data']
#         for res5 in res4: # # res4 in data list     
#             final_result = res5['results']
#             final_result.append(data_result)


#     for tcm2 in tcm_template['testcatalogmanager']['ut']['tests']:
#         for tcm3 in tcm2:
#             tcm3 = final_result


#     data = [{
#         "uuid": str(uuid),
#         "name": str(tag + "_" + testName + "_" + str(datetime.datetime.utcnow())),
#         "verdict": str(totalResult),
#         "result": tcm3
#     }]

#     for tcm2b in tcm_template['testcatalogmanager']['ut']['tests']:
#         tcm2b['data'] = data

#     pymongoTest.updateTCMTemplate(mongoIP, 'logs', 'TestCatalogManager', template_uuid, tcm_template['testcatalogmanager'])
#     ##

#     #return results to swagger
#     swagger_results = pymongoTest.fetchDocWithUUID(mongoIP, 'logs', 'TestCatalogManager', 'Rocket', template_uuid)
#     return swagger_results
#     ###

# def get_validation(body):
#     log.debug('post it')
#     # return ("Valid Input")
#     # hgi = "2000"
#     # return hgi
#     # return {
#     #     'post': name
#     # }


# def get_execution(body):
#     log.debug('post it')
#     # return json.dumps(r, indent=2)
#     # return {
#     #     'delete': name
#     # }