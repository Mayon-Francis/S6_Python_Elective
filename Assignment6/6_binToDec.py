binStr = input("Enter a binary number: ")

integerPart = binStr.split(".")[0]
fractionalPart = binStr.split(".")[1]
decStr = 0

for idx, c in enumerate(integerPart):
    decStr += float(c) * 2**(len(integerPart) - idx - 1)

for idx, c in enumerate(fractionalPart):
    decStr += float(c) * 2**(-idx - 1)

print(decStr)
