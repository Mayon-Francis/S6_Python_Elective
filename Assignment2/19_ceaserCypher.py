inpStr = input("Enter a string: ")
inpKey = int(input("Enter a key: "))
outStr = ""

for c in inpStr:
    if(c.isupper()):
        outStr += chr((ord(c) + inpKey - 65) % 26 + 65)
    elif(c.islower()):
        outStr += chr((ord(c) + inpKey - 97) % 26 + 97)
    else:   
        print("Only Alphabets are allowed")
        exit()

print("CipherText:" + outStr)

# Decrypt above ceaser Cypher
print("Decrypted Text: ", end="")
for c in outStr:
    if(c.isupper()):
        print(chr((ord(c) - inpKey - 65) % 26 + 65), end="")
    else:
        print(chr((ord(c) - inpKey - 97) % 26 + 97), end="")

print("\n")
