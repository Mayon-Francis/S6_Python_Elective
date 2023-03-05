n = int(input("Enter a number: "))
nCopy = n
binary = ""
while n > 0:
    binary = str(n % 2) + binary
    n = n // 2

print(f"Binary of {nCopy} is {binary}")
