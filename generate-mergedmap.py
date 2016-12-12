import sys
import os
import csv
import numpy as np

csvFilename = "merge-heatmap.csv"

runnerFilename = "route-frequencymap-medium.csv"
treeFilename = "trees-frequencymap.csv"
pedestrianFilename = "pedestrian-frequencymap.csv"

latIndex = 0
longIndex = 1
freqIndex = 2

runnerMap = {}
treeMap = {}
pedestrianMap = {}

csvFile = open(runnerFilename, 'r')
reader = csv.reader(csvFile, delimiter=',', quotechar='|')
reader.next()
for line in reader:
    pos = (round(float(line[latIndex]), 3), round(float(line[longIndex]),3))
    if pos not in runnerMap: runnerMap[pos] = 0
    runnerMap[pos] += float(line[freqIndex])
csvFile.close()

csvFile = open(treeFilename, 'r')
reader = csv.reader(csvFile, delimiter=',', quotechar='|')
reader.next()
for line in reader:
    pos = (round(float(line[latIndex]),3), round(float(line[longIndex]),3))
    if pos not in treeMap: treeMap[pos] = 0
    treeMap[pos] += float(line[freqIndex])
csvFile.close()

csvFile = open(pedestrianFilename, 'r')
reader = csv.reader(csvFile, delimiter=',', quotechar='|')
reader.next()
for line in reader:
    pos = (round(float(line[latIndex]),3), round(float(line[longIndex]),3))
    if pos not in pedestrianMap: pedestrianMap[pos] = 0
    pedestrianMap[pos] += float(line[freqIndex])
csvFile.close()

squareMap = {}
counter = 0

csvfile = open(csvFilename, 'wb')
writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
writer.writerow(['latitude', 'longitude', 'runners', 'trees', 'pedestrians'])

counter = 0
for point in runnerMap.items():
    treeVal = 0
    if point[0] in treeMap: treeVal = treeMap[point[0]]
    pedestrianVal = 0
    if point[0] in pedestrianMap: pedestrianVal = pedestrianMap[point[0]]
    writer.writerow([point[0][0], point[0][1], round(point[1]), round(treeVal), round(pedestrianVal)])
    counter += 1
    if counter % 100 is 0: print("Points processed: {0}".format(counter))

csvFile.close()
exit()

counter = 0
for point in runnerMap.items():
    closestTree = (-1,-1)
    for tree in treeMap.items():
        distance = ((point[0][0] - tree[0][0])**2 + (point[0][1] - tree[0][1])**2)**(1/2.0)
        if closestTree[0] == -1 or distance < closestTree[0]: closestTree = (distance, tree[1])
    closestPedestrian = (-1, -1)
    for pedestrian in treeMap.items():
        distance = ((point[0][0] - pedestrian[0][0])**2 + (point[0][1] - pedestrian[0][1])**2)**(1/2.0)
        if closestPedestrian[0] == -1 or distance < closestPedestrian[0]: closestPedestrian = (distance, pedestrian[1])
    writer.writerow([point[0][0], point[0][1], round(point[1]), round(closestTree[1]), round(closestPedestrian[1])])
    counter += 1
    if counter % 100 is 0: print("Points processed: {0}".format(counter))

csvFile.close()
