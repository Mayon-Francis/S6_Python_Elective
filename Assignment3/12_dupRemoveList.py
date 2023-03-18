l = [10, 20, 20, 30, 40]
s = set(l)
dupRem = list(s)
print("Duplicates removed: ",sorted(dupRem))

# If duplicate present, remove it altogether
for i in l: 
    if l.count(i) > 1:
        l = [x for x in l if x != i]

print("Duplicates removed altogether: ", l)