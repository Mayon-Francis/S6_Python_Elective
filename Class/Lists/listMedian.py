def mean(l):
    return sum(l)/len(l)

def median(l):
    l = l.copy()
    l.sort()
    length = len(l)
    if length % 2 == 0:
        return (l[length//2] + l[length//2 - 1])/2
    else:
        return l[length//2]

n = int(input("Enter the number of elements: "))

l = list()

for i in range(n):
    l.append(int(input("Enter the element {}: ".format(i+1))))

print(l)
print(*l)
print("mean: ", mean(l))
print("median: ", median(l))
print("max: ", max(l))
print("min: ", min(l))
print(l)
