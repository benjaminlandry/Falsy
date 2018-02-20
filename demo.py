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

import pymongoConnect
import collections
import bson
import xmltodict
#from xmljson import badgerfish as bf

log = JLog().bind()

def get_it(resource, responder):
    log.debug('get it')
    url2 = 'http://142.133.174.149:8888' + '/' + resource + '?' +responder + '&format=xml'
    #url2 = 'http://142.133.174.149:8888/AfgBsfIpv6TestCases.TestCase0020SuccessAfgBsfUc100GussTimestampNotEnabled?test&format=xml'
    print(url2)

    parameters = {'resource': resource, 'responder':responder}
    r = requests.get(url2, parameters)
    data = r.text
    
    #### mongo ###
    #TODO: convert data to Bson, Json or Dict. Then input data into postToMongo(XXX)


    dataInJson = xmltodict.parse(data)
    #print(dataInJson)
    #pymongoConnect.postToMongo(dataInJson)
    #testInfo = pymongoConnect.fetchFromMongo()
    #print(testInfo)

    client = MongoClient('172.17.0.2', 27017) # connects client with the mongoserver
    FT = client['FT'] # create a database
    RBT = FT['RBT'] # create a collection

    RBT.insert_one(dataInJson) # insert a log document 
    x = RBT.find_one({"testResults": 1}) # fetch a document
    print(x)

    ### mongo ##
    f = open('Test_logs.xml', 'w') # in string-format
    f.write(data)
    f.close()

    infile = open("Test_logs.xml","r")
    contents = infile.read()
    soup = BeautifulSoup(contents,'xml')
    hi = soup.get_text()
    return hi

    # xmlDoc = open('Test_logs.xml', 'r')
    # xmlDocData = xmlDoc.read()
    # xmlDocTree = etree.XML(xmlDocData)

    # for ingredient in xmlDocTree.iter('runTimeInMillis'):
    #     print(ingredient[0].text)
        # return ingredient[0].string
        



    # return data

















#     return {
#         'get': name
#     }

# def get(self, resource, responder, tag):
#         '''TC#1 Definition'''
#         url2 = 'http://' + host +  port + '/' + resource + '?' +responder + '&format=xml&includehtml'
#         #url2 = 'http://142.133.174.149:8888/AfgBsfIpv6TestCases.TestCase0020SuccessAfgBsfUc100GussTimestampNotEnabled?test&format=xml'
#         print(url2)



#         url = 'http://httpbin.org/get'
#        # url = 'http://142.133.174.149:8888/AfgApTestCases.TestCase0800SuccessAfgApAutGbaDigest?test'
#         tag = tag   # TODO: tag goes to a grouping file. Grouping would be done backend and hardcoded.
#         parameters = {'resource': resource, 'responder':responder, 'tag': tag}
#         r = requests.get(url2, parameters)
#         data = r.text

#         # root = etree.fromstring(r)
#         # etree.tostring(root)
#         #tree = etree.parse(StringIO(r))
#         # tree = etree.parse("country_data2.xml")
#         # etree.tostring(tree.getroot())

#         #jsonData = json.dumps(r)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
#         #with open('Tests_Logs.txt', 'a') as outfile:
#         #dumps(bf.data(fromstring(data)))
#         #    json.dump(jsonData, outfile, sort_keys = False, indent = 4,
#         #       ensure_ascii = False)





# #################
#         f = open('Test_logs.xml', 'w') # in string-format
#         f.write(data)
#         f.close()

#         infile = open("Test_logs.xml","r")
#         contents = infile.read()
#         soup = BeautifulSoup(contents,'xml')
#         hi = soup.get_text()
# ##################
#         return hi
#         #return data



def post_it(name):
    log.debug('post it')
    return {
        'post': name
    }


def delete_it(name):
    return {
        'delete': name
    }


def put_it(name):
    return {
        'put': name
    }


def patch_it(name):
    return {
        'patch': name
    }
