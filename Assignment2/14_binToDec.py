binInput = input("Enter a binary number: ")
decOutput= 0
print("The decimal value of the binary number is: ", int(binInput, 2))

for b in binInput:
    if b not in ['0', '1']:
        print("Invalid binary number")
        break
    decOutput = decOutput * 2 + int(b)

print("The decimal value of the binary number is: ", decOutput)