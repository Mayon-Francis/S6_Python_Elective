n = int(input("Enter value: "))

if (n & (n - 1)) == 0:
    print("Power of 2")
else:
    print("Not power of 2")