import datetime
import pymongo
from pymongo import MongoClient
import pprint

from falsy.jlog.jlog import JLog
import requests

import json
import xml.etree.ElementTree
from json import dumps
import uuid
# from xmljson import badgerfish as bf
# import xml.etree.ElementTree as ET
import xml.etree.cElementTree as etree
import re
from lxml import etree
from io import StringIO, BytesIO
from bs4 import BeautifulSoup

import xmltodict
import pymongoTestCode


log = JLog().bind()


def get_it_TC(TestCaseName, TestCaseNumber, Tag):
    log.debug('get it')    

     ## new edits
    
    fetchedCase = pymongoTestCode.fetchUrlFromMongo_Case('FT', 'RBT', 'AFG', 'AfgOpenIdConnectTestCases', 'TestCase0700SuccessAfgOpenIdConnectFeatureDisable')


    # database = 'FT'
    # collection = 'RBT'
    #fetchedResults = pymongoTestCode.fetchUrlFromMongo_Suite(database, collection, Tag, TestCaseName, TestCaseNumber)
    print(fetchedSuite['url'])
    print(fetchedCase['url'])


    r = requests.get(fetchedResults['url'])
    data = r.text

    ## mongo ##
    dataInJson = xmltodict.parse(data)
    print(dataInJson)
    logs = pymongoTestCode.postTestLogsToMongo(dataInJson)
    print(logs)

    ###
   
    f = open('Test_logs.xml', 'w')
    f.write(data)
    f.close()
    infile = open("Test_logs.xml","r")
    contents = infile.read()
    soup = BeautifulSoup(contents,'xml')
    hi = soup.get_text()
    return hi


def get_it_TS(TestSuiteName, Tag):
    log.debug('get it')

     ## new edits
    fetchedSuite = pymongoTestCode.fetchUrlFromMongo_Suite('FT', 'RBT', 'AFG', 'AfgOfflineLicenseTestSuites', 'TestSuiteAfgOpenIdOfflineLicense')


    # database = 'FT'
    # collection = 'RBT'
    #fetchedResults = pymongoTestCode.fetchUrlFromMongo_Suite(database, collection, Tag, TestName)
    print(fetchedSuite['url'])

    r = requests.get(fetchedResults['url'])
    data = r.text

    ## mongo ##
    dataInJson = xmltodict.parse(data)
    print(dataInJson)
    logs = pymongoTestCode.postTestLogsToMongo(dataInJson)
    print(logs)

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