import random
import matplotlib as mat

import matplotlib.pyplot as plt
import Point

# creating the data set
dataSet = [Point(1,1)]

num = int(input("How many data points should there be?"))

dataSet.append(Point(1,1))

for i in range(num):
    #dataSet.append(Point(i,i))
    i = i+1
    #dataSet[0].append(random.random())
    #dataSet[1].append(random.random())

plt.plot(dataSet)
plt.show()