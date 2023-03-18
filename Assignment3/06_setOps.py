A = set()
print("Enter numbers for set A: ")
for i in range(5):
    A.add(int(input("> ")))
B = set()
print("Enter numbers for set B: ")
for i in range(5):
    B.add(int(input("> ")))

print("A: ", A)
print("B: ", B)
print("A union B: ", A.union(B))
print("A intersection B: ", A.intersection(B))
print("A Symmetric difference B: ", A.symmetric_difference(B))