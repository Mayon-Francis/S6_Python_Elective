l =list()
l = [0,9,"k", 2+3j]

print(l)
print(type(l))
print(type(l[3]))
print(l[1:3])

l2 = list(range(10,20,2))
print(l2)

# import numpy as np
array1=list([10,12,14,16,18,20,22])
print(array1[1:5:2])
print(array1[-4:])

print(len(array1))
print(max(array1))
print(min(array1))
print(sum(array1))
print(sum(array1)/len(array1))

# Insert to list
array1 = array1 + [24]
print(array1)
array1 = [24] + array1
print(array1)
array1.insert(1,26)
print(array1)
array1.append(100)
print(array1)
array1.extend([100,22])
print(array1)

# sort
array1.sort(reverse=True)
print(array1)
array1.pop()
print(array1)
print(dir(array1))
print(array1.count(100))

array1.clear()
print(array1)