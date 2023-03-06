s = {10,20,30, 10}
print(s)
# print(s[0])   TypeError: 'set' object does not support indexing

s2= {20, 30, 40, 50}

print("union: ", s.union(s2))
print("union: ", s | s2)
print("intersection: ", s.intersection(s2))
print("intersection: ", s & s2)
print("difference: ", s.difference(s2))
print("difference: ", s - s2)

# symmetric diff: elements in either set, but not both
# (s-s2) | (s2-s)
print("symmetric difference: ", s.symmetric_difference(s2))
print("symmetric difference: ", s^s2)

# check if subset
print("s is subset of s2: ", s.issubset(s2))
