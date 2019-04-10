def jsontester(resp, resultdict):
    data = resp.json()

    #resultdict contains the types and the names of what should be in the response
    i = 0
    while i < len(data):
        # this checks to make sure that the keys are correct and that they have the correct types
        for item in resultdict:
            assert (item in data[i])
            assert (type(data[i][item]) is resultdict[item])
        i = i + 1