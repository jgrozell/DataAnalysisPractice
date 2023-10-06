import random
import matplotlib as mat

import matplotlib.pyplot as plt
from Point import Point

point1 = Point(1,1)

# creating the data set
dataSet = []

num = int(input("How many data points should there be?"))

dataSet.append(Point(1,1))

for i in range(num):
    #dataSet.append(Point(i,i))
    print('hello')
    #dataSet[0].append(random.random())
    #dataSet[1].append(random.random())

plt.plot(dataSet)
plt.show()