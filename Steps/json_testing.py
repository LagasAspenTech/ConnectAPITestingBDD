import requests
import json
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

def jsontester(data, resultdict):
    #resultdict contains the types and the names of what should be in the response
    #for example, {"deviceName": str, "versionNumber": str, "macAddress": str, "ipAddress": str, "lastBroadcast": int}
    #print(data) #this is for debug purposes
    i = 0
    if (isinstance(data, list) is False):
        data = [data]
    while i < len(data):
        # this checks to make sure that the keys are correct and that they have the correct types
        for item in resultdict:
            print(item)
            assert (item in data[i])
            if resultdict[item] == "num":
                assert (isinstance(data[i][item], (int, float, complex)))
            else:
                assert (type(data[i][item]) is resultdict[item])
        i = i + 1

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