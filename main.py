__author__ = "Rizky Solechudin"
from data import load
import numpy as np

filename = "./data/dataset.csv"
rawData = load.loadData(filename)
headers = load.getHeaders(rawData)
data = load.createDict(rawData)

i = 0
for head in headers:
    print(i, data[head])
    i += 1 

print("asma1, fitur 1", data["asma1"][2])