# Read names and sort them

n = int(input("Enter the number of elements: "))

l = list()

for i in range(n):
    l.append(input("Enter the Name: "))

l.sort()
print("Sorted list:",l)

l.sort(key=len)
print("Sorted list:",l)