import math

numList = []
print("Enter 5 numbers: ")
for i in range(5):
    numList.append(int(input("> ")))
mean = sum(numList)/len(numList)
print("Mean: ", mean)
numList.sort()
if len(numList) % 2 == 0:
    median = (numList[len(numList)//2] + numList[len(numList)//2 - 1])/2
else:
    median = numList[len(numList)//2]
print("Median: ", median)
var  = sum(pow(x-mean,2) for x in numList) / len(numList) 
print("Standard Deviation: ", math.sqrt(var)  )

import statistics
print("OR: Standard Deviation: ", statistics.stdev(numList))

