import sys
import os
import csv
import numpy as np

squareWidth = float(sys.argv[1])
inputFile = sys.argv[2]
x1 = float(sys.argv[3])
y1 = float(sys.argv[4])
x2 = float(sys.argv[5])
y2 = float(sys.argv[6])
csvFilename = "pedestrian-frequencymap.csv"
csvLongCol = "LONGITUDE"
csvLatCol = "LATITUDE"
csvValCol = "CNT_TOTAL"

inputMap = {}

csvfile = open(inputFile, 'r')
reader = csv.reader(csvfile, delimiter=',', quotechar='|')

i = 0;
for header in reader.next():
    if header == csvLongCol:
        csvLongCol = i
        print("Hit!")
    if header == csvLatCol:
        csvLatCol = i
        print("Hit!")
    if header == csvValCol:
        csvValCol = i
        print("Hit!")
    i += 1

for row in reader:
    pos = (float(row[csvLatCol]), float(row[csvLongCol]))
    if pos not in inputMap: inputMap[pos] = 0
    inputMap[pos] += float(row[csvValCol])

squareMap = {}
counter = 0
for point in [(a,b) for a in np.arange(x1, x2, squareWidth) for b in np.arange(y1, y2, squareWidth)]:
    squareMap[point] = 0
    closest = (-1, 0.)
    for sensor in inputMap.items():
        distance = ((point[0] - sensor[0][0])**2 + (point[1] - sensor[0][1])**2) ** (1/2.0)
        distance = distance / squareWidth
        if closest[0] == -1 or distance < closest[0]: closest = (distance, sensor[1])
        squareMap[point] += min(1 / distance, 1) * sensor[1]
        counter += 1
        if counter % 1000 is 0:
            print("Points processed: {0}".format(counter))
    squareMap[point] = int(squareMap[point])
    squareMap[point] = int(min(squareMap[point], closest[1]))
    #if squareMap[point] < 100: del squareMap[point]

csvfile = open(csvFilename, 'wb')
writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
writer.writerow(['latitude', 'longitude', 'frequency'])
for entry in squareMap.items():
    writer.writerow([entry[0][0], entry[0][1], entry[1]])

csvfile.close()
