n = input("Enter a string: ")

print("String after swapping case: ", end="")

for c in n:
    if c.islower():
        print(c.upper(), end="")
    elif c.isupper():
        print(c.lower(), end="")
    else:
        print(c, end="")

print()