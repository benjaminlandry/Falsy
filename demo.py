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


client = MongoClient('172.17.0.2', 27017) # connects client with the mongoserver
FT = client['FT'] # create ahh database
RBT = FT['RBT'] # create a collection


log = JLog().bind()

def get_it(TestCaseName, TestCaseNumber, tag):
    log.debug('get it')
    fetchedResults = fetchUrlFromMongo(RBT1, 'AFG', 'AfgOfflineLicenseTestSuites', 'TestSuiteAfgOpenIdOfflineLicense')
    #fetchedResults = fetchUrlFromMongo(collection, Tag, ClassDefinition, FunctionDefinition)
    print(fetchedResults["url"])


    r = requests.get(fetchedResults['url'])
    data = r.text

    ## mongo ##
    dataInJson = xmltodict.parse(data)
    print(dataInJson)
    logs = pymongoTestCode.postTestLogsToMongo(dataInJson)
    print(logs)

    
    ##

    f = open('Test_logs.xml', 'w') # in string-format
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
