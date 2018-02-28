import datetime
import pymongo
from pymongo import MongoClient
import pprint

from falsy.jlog.jlog import JLog
import requests

import json
import xml.etree.ElementTree
from json import dumps
# from xmljson import badgerfish as bf
# import xml.etree.ElementTree as ET
import xml.etree.cElementTree as etree
import re
from lxml import etree
from io import StringIO, BytesIO
from bs4 import BeautifulSoup

import xmltodict
import pymongoTest 
import uuid
from bson import ObjectId
from uuid import UUID

#logger
log = JLog().bind()

#TS

#TODO: fetch actual UUID from mongo-live
uuid = ObjectId("5a908064d5b67f3dd2e630ae")
template_uuid = ObjectId("5a956fb1d5b67f11e0ded6e6")
logData = pymongoTest.fetchResultsFromOneLog('logs', 'TestLogs', uuid)
tcm_template = pymongoTest.fetchResultsFromOneLog('logs', 'TestCatalogManager', template_uuid)

#verdict
totalResult_right = logData['testResults']['finalCounts']['right']
totalResult_wrong = logData['testResults']['finalCounts']['wrong']

if (totalResult_wrong == '0') and (totalResult_right >= 0):
    totalResult = 'Success'
else:
    totalResult = 'Failure'
#print(totalResult)

#TODO: append data to data in tcm_template
data = {
    "uuid": str(uuid),
    #"name": str(tag + "_" + testName + "_" + datetime.datetime.utcnow()),
    "verdict": str(totalResult)
}
print(data)

res2 = tcm_template['testcatalogmanager']['ut']['tests']
for res3 in res2:
    res4 = res3['data']
    for res5 in res4: # # res4 in data list     
        print(res5['results'])


for x in logData['testResults']['result']:
    #Test_case
    Test_Case = (x['relativePageName'])
    #Test_result
    result_right = (x['counts']['right'])
    result_wrong = (x['counts']['wrong'])

    if (result_wrong == '0') and (result_right >= 0):
        result = 'Success'
    else:
        result = 'Failure'
    print(result)
    #Time Evaluation
    duration = (x['runTimeInMillis'])
    print(duration)


    #JSON-body
    # original_json = json.load(open('tcm_template.json'))
    
    #TODO: add append for-loop
    #TODO: update mongo-JSON with response_results
    data_result = {
        "Test_Case": str(Test_Case),
        "Test_Result": str(result),
        "Time Evaluation": str(duration)
    }
    # tcm_template['testcatalogmanager']['ut'][0]['data']['results'].append(data_result)
    #print(original_json)


#response_json = data + data_results + response_json    
#print(json.dumps(response_json, indent=2))








def get_it_TC(TestCaseName, TestCaseNumber, Tag):
    log.debug('get it')    

    ## mongo ##
    
    fetchedCase = pymongoTest.fetchUrlFromMongo_Case('FT', 'RBT', 'AFG', 'AfgOpenIdConnectTestCases', 'TestCase0700SuccessAfgOpenIdConnectFeatureDisable', '0700')

    # database = 'FT'
    # collection = 'RBT'
    # fetchedCase = pymongoTest.fetchUrlFromMongo_Suite(database, collection, Tag, ClassDefinition, TestCaseName, TestCaseNumber)
    # print(fetchedCase['url'])

    ## requests ##
    r = requests.get(fetchedCase['url'])
    data = r.text
    #appendData = {str(uuid.uuid4())} + r.text
    dataInJson = xmltodict.parse(data)
    print(dataInJson)
    #print(dataInJson)
    ## append data
    

    ## logs
    
    #pymongoTest.postTestLogsToMongo('logs', 'TestLogs', dataInJson)
    #print(str(uuid.uuid4()))
    uuid = ObjectId("5a8ee5fdd5b67f1d6831c50a")
    logData = pymongoTest.fetchResultsFromOneLog('logs', 'TestLogs', uuid)
    print(logData)
    ###
   
    # f = open('Test_logs.xml', 'w')
    # f.write(data)
    # f.close()
    # infile = open("Test_logs.xml","r")

    # contents = infile.read()
    # soup = BeautifulSoup(contents,'xml')
    # hi = soup.get_text()
    return logData


def get_it_TS(TestSuiteName, Tag):
    log.debug('get it')

    ## mongo ##

    fetchedSuite = pymongoTest.fetchUrlFromMongo_Suite('FT', 'RBT', 'AFG', 'AfgOfflineLicenseTestSuites', 'TestSuiteAfgOpenIdOfflineLicense')

    database = 'FT'
    collection = 'RBT'
    #fetchedSuite = pymongoTest.fetchUrlFromMongo_Suite(database, collection, Tag, ClassDefinitionTestSuiteName)
    print(fetchedSuite['url'])

    ## requests ##
    r = requests.get(fetchedSuite['url'])
    data = r.text
    dataInJson = xmltodict.parse(data)
    print(dataInJson)
    pymongoTest.postTestLogsToMongo('logs', 'TestLogs', dataInJson)

    ###

    f = open('Test_logs.xml', 'w')
    f.write(data)
    f.close()
    infile = open("Test_logs.xml","r")
    contents = infile.read()
    soup = BeautifulSoup(contents,'xml')
    hi = soup.get_text()
    return hi



def post_it(name):
    log.debug('post it')
    return {
        'post': name
    }

def put_it(name):
    return {
        'put': name
    }