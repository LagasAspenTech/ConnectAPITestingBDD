#json_testing.py contains code for various functions and classes that are used in tests but are not tests in and of themselves

import requests
import json

#twooutputs compares a response containing a list of multiple json items to two valid output jsons. If the names and keys of something in the response match one of the two output jsons, they are then compared
def twooutputs(output_json_1, output_json_2, respholder):
    result = respholder.getResp().json()
    output_1 = json.loads(output_json_1)
    output_2 = json.loads(output_json_2)
    for item in result:
        if item != {}:
            if item["key"] == output_1["key"] and item["name"] == output_1["name"]:
                compare_ouput_json(output_1, item)
            elif item["key"] == output_2["key"] and item["name"] == output_2["name"]:
                compare_ouput_json(output_2, item)


#jsontester compares the types of an element in a json to a dictionary listing what the types of the elements in the json should be. Only use this if you don't know what the actual values of the elements should be
def jsontester(data, resultdict):
    #resultdict contains the types and the names of what should be in the response
    #for example, {"deviceName": str, "versionNumber": str, "macAddress": str, "ipAddress": str, "lastBroadcast": int}
    i = 0
    if (isinstance(data, list) is False):
        data = [data]
    while i < len(data):
        # this checks to make sure that the keys are correct and that they have the correct types
        for item in resultdict:
            assert (item in data[i])
            if resultdict[item] == "num":
                assert (isinstance(data[i][item], (int, float, complex)))
            else:
                assert (type(data[i][item]) is resultdict[item])
        i = i + 1

#compare output json compares a json response to the expected json response and makes sure they are equal. Token is variable, so that is ignored.
def compare_ouput_json(expected, result):
    for item in result:
        assert (item in expected)
        if item == "objectId" or item == "id":
            if expected[item] == 0:
                assert (result[item] > expected[item])
            else:
                assert (result[item] == expected[item])
        elif item != "token":
            assert(expected[item] == result[item])

#memoryclass is used to store values that need to be referenced in multiple tests which change each time the tests are run, such as server IDs or route IDs
#this is why tags, routes, servers, and so on, are referenced not by ID in the test cases, but by the order of initialization
class memoryclass:
    def __init__(self):
        self.serverIDs = []
        self.routeIDs = []
        self.schemas = []
        self.tagIDs = {0:[]}
        self.dertagIDs = {0:[]}
    def getServerId(self, i):
        return(self.serverIDs[i])
    def getServerIds(self):
        return(self.serverIDs)
    def addServer(self, i):
        self.serverIDs.append(i)
    def addRoute(self, i):
        self.routeIDs.append(i)
    def getRoute(self, i):
        return(self.routeIDs[i])
    def addTag(self, server, tag):
        if server in self.tagIDs:
            self.tagIDs[server].append(tag)
        else:
            self.tagIDs[server] = [tag]
    def getTag(self, x, y):
        return(self.tagIDs[x][y])
    def getTags(self, x):
        return(self.tagIDs[x])
    def getallTags(self):
        return(self.tagIDs)
    def addDerTag(self, server, tag):
        if server in self.dertagIDs:
            self.dertagIDs[server].append(tag)
        else:
            self.dertagIDs[server] = [tag]
    def getDerTag(self, x, y):
        return(self.dertagIDs[x][y])
    def getDerTags(self, x):
        return(self.dertagIDs[x])
    def getallDerTags(self):
        return(self.dertagIDs)
    def addSchema(self, newschema):
        self.schemas.append(newschema)
    def getSchemas(self):
        return(self.schemas)

#respclass sends out requests to the server and stores the response
class respclass:
    def __init__(self, URL, RESP):
        self.url = URL
        self.resp = RESP
    def getResp(self):
        return self.resp
    def setResp(self, type, param=None, post=None):
        if param is None and post is None:
            self.resp = requests.get('http://' + self.url + type)
        elif param is not None and post is not None:
            self.resp = requests.post('http://' + self.url + type, params=param, data=post)
        elif param is None and post is not None:
            self.resp = requests.post('http://' + self.url + type, data=post)
    def setURL(self, URL):
        self.url = URL
    def getURL(self):
        return self.url