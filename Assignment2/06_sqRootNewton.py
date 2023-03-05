n = int(input("Enter a number: "))
x = n
# To count the number of iterations
count = 0

while (1) :
    count += 1
    # Calculate more closed x
    root = 0.5 * (x + (n / x))
    # Check for closeness
    if (abs(root - x) < 0.00001) :
        break
    # Update root
    x = root

print("The square root of", n, "is", root)