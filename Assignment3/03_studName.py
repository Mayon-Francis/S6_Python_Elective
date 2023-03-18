n = int(input("Enter number of names: "))
names = list()
for i in range(n):
    names.append(input("Enter name: "))

names.sort()
print("Names in Alphabetical Order:", names)
print("Name with maximum length:", max(names, key=len))
print("Names starting with A:", [name for name in names if name[0] == "A"])
names = [name.upper() for name in names]
print("Names in Uppercase:", names)
names.reverse()
print("Reverse: ", names)
names.sort(key=len)
print("Names sorted by length:", names)