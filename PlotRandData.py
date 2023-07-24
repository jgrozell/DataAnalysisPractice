import random
import matplotlib as mat
import matplotlib.pyplot as plt
import Point, LineString, Polygon

# creating the data set
dataSet = []

num = int(input("How many data points should there be?"))

for i in range(num):
    dataSet.append(Point(random.random(), random.random()))
    
    #dataSet[0].append(random.random())
    #dataSet[1].append(random.random())

plt.plot(dataSet)
plt.show()