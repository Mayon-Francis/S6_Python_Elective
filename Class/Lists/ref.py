
# for deep copy
import copy

l1 = [10,20,30]
# l2 is not a copy of l1, it is a reference to l1
l2 = l1
print(l1, l2)

l1[0] = 100
print(l1, l2)

# id is like a unique address of the object, similar to a pointer
print (id(l1), id(l2))

l2.append(40)
print(l1, l2)

# now copy
l3 = l1.copy()
print(id(l1), id(l3))
l3.append(50)
print(l1, l3)

# deep copy
l4 = copy.deepcopy(l1)
print(id(l1), id(l4))
