t = (20)
print(type(t))
t=(20,)
print(type(t))

t = t + (30,)
print(t)

# Error
# t = t+(30)
# print(t)

t += (40,50,60)

print("tuple", t)
print(t[0])
print(t[1:3])
print(t[1:])
print(t[:3])

# Error, tuples are immutable, does not support item assignment
# t[0] = 100
print(t)
print(min(t))
print(max(t))

# Tuple Packing
t1 = (101, 'hello, world', 3.14)
# Tuple Unpacking
num, msg, pi = t1
print(num, msg, pi)

t2 = (102, "bye, world", 2.71)

l = [t1, t2]
print(l)

# tuple exchange
print(t1, t2)
t1, t2 = t2, t1
print(t1, t2)


print(t.index(20))



print("***************************")
print(l)
# sorts according to the first element
l.sort()
print(l)

l.sort(key=lambda x: x[1])
print(l)
