import requests

def jsontester(data, resultdict):
    #resultdict contains the types and the names of what should be in the response
    #for example, {"deviceName": str, "versionNumber": str, "macAddress": str, "ipAddress": str, "lastBroadcast": int}
    #print(data) #this is for debug purposes
    i = 0
    if (isinstance(data, dict) is False):
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
            assert (result[item] > expected[item])
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
            #print(self.resp.json())
    def setURL(self, URL):
        self.url = URL
    def getURL(self):
        return self.url