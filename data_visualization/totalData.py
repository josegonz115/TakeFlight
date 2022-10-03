import pandas as pd
from matplotlib import pyplot as plt
import os


arrayOfDicts = []

folderPath = "waterLevelsWaxLakeOutlet\\PreDeltaX_Water_Level_Data_1801\\data"


latitudeTotal = []
longitudeTotal = [] 
absWaterLevel = []

dataDict = {"year": [], "long": [], "lat": [], "level": []}

for file in os.listdir(folderPath):
    if ".csv" in file:
        data = pd.read_csv(
            "waterLevelsWaxLakeOutlet\\PreDeltaX_Water_Level_Data_1801\data\\" + file)
        latitude = data.latitude
        latitudeTotal.append(latitude)
        longitude = data.longitude
        longitudeTotal.append(longitude)
        absWaterlvl = data.absolute_water_level_NAVD88
        absWaterLevel.append(absWaterlvl)

count = 0
for item in latitudeTotal:
    for line in item:
        count += 1
        dataDict["lat"].append(round(line, 3))
        #dataDict["lat"].append(line)
dataDict["year"].append([2016] * count)

for file in longitudeTotal:
    for line in file:
        dataDict["long"].append(round(line, 3))
        #dataDict["long"].append(line)

for file in absWaterLevel:
    for line in file:
        dataDict["level"].append(line)


#arrayOfDicts.append(dataDict)
for i in range(len(dataDict['long'])):
    myDict = {
        "year": 2016,
        "long": dataDict.get("long")[i],
        "lat": dataDict.get("lat")[i],
        "level": dataDict.get("level")[i]
    }
    arrayOfDicts.append(myDict)

# Extracting from 2015 Wax Lake Outlet.
dataDict2 = {"year": [], "long": [], "lat": [], "level": []}

latBefore = []
longBefore = []
levelBefore = []

for file in os.listdir("waxLakeOutlet2015\\data"):
    data = pd.read_csv("waxLakeOutlet2015\\data\\" + file)
    lat = data.latitude
    latBefore.append(lat)
    long = data.longitude
    longBefore.append(long)
    waterlvl = data.water_surface_elevation_NAVD88
    levelBefore.append(waterlvl)

count = 0
for item in latBefore:
    for line in item:
        count += 1
        dataDict2["lat"].append(round(line, 3))
        #dataDict2["lat"].append(line)
dataDict2["year"].append([2015] * count)


for file in longBefore:
    for line in file:
        dataDict2["long"].append(round(line, 3))
        #dataDict2["long"].append(line)

for file in levelBefore:
    for line in file:
        dataDict2["level"].append(line)

#arrayOfDicts.append(dataDict2)
for i in range(len(dataDict2['long'])):
    myDict = {
        "year": 2015,
        "long": dataDict2.get("long")[i],
        "lat": dataDict2.get("lat")[i],
        "level": dataDict2.get("level")[i]
    }
    arrayOfDicts.append(myDict)
# 374