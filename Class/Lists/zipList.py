l1 = [1,2,3]
l2 = [4,5,6]

z = zip(l1,l2)
print(z)
# Can't use the iterator more than once: as it returns an iterator
# print("Each element of z is a tuple:")
# for i in z:
#     print(i)
zList = print(list(z))
print(zList)