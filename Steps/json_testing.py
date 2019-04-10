import requests

def jsontester(data, resultdict):
    #resultdict contains the types and the names of what should be in the response
    #for example, {"deviceName": str, "versionNumber": str, "macAddress": str, "ipAddress": str, "lastBroadcast": int}
    print(data) #this is for debug purposes
    i = 0
    while i < len(data):
        # this checks to make sure that the keys are correct and that they have the correct types
        for item in resultdict:
            assert (item in data[i])
            if resultdict[item] == "num":
                assert (isinstance(data[i][item], (int, float, complex)))
            else:
                assert (type(data[i][item]) is resultdict[item])
        i = i + 1

class respclass:
    def __init__(self, URL, RESP):
        self.url = URL
        self.resp = RESP
    def getResp(self):
        return self.resp
    def setResp(self, type):
        self.resp = requests.get('http://' + self.url + type)
    def setURL(self, URL):
        self.url = URL
    def getURL(self):
        return self.url