t = ()
print("Enter 10 numbers: ")

for i in range(10):
    t += (int(input("> ")),)

print("Tuple:", t)
print("Sum: ", sum(t))
print("Avg: ", sum(t)/len(t))
print("Max: ", max(t))
print("Min: ", min(t))
