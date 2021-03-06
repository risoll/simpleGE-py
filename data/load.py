import numpy as np

def loadData(filename):
    data = np.loadtxt(filename, delimiter=",", dtype=str)
    return data

def getHeaders(data):
    return [x.strip("b'") for x in data[:,0]]

def createDict(data):
    headers = getHeaders(data)
    newDict = {}
    i = 0
    data = data[:,1:len(data)]
    for head in headers:
        newDict[head] = [float(x.strip("b'")) for x in data[i]]
        i += 1
    return newDict