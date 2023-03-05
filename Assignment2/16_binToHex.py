def binToHex(bin):
    hex = ""
    for i in range(0, len(bin), 4):
        hex += str(hexConv(bin[i:i+4]))
    return hex
def hexConv(bin):
    if bin == "0000":
        return 0
    elif bin == "0001":
        return 1
    elif bin == "0010":
        return 2
    elif bin == "0011":
        return 3
    elif bin == "0100":
        return 4
    elif bin == "0101":
        return 5
    elif bin == "0110":
        return 6
    elif bin == "0111":
        return 7
    elif bin == "1000":
        return 8
    elif bin == "1001":
        return 9
    elif bin == "1010":
        return "A"
    elif bin == "1011":
        return "B"
    elif bin == "1100":
        return "C"
    elif bin == "1101":
        return "D"
    elif bin == "1110":
        return "E"
    elif bin == "1111":
        return "F"
n = input("Enter an 8 bit binary number: ")
if len(n) != 8:
    print("Invalid input")
else:
    print(f"Hexadecimal of {n} is {binToHex(n)}")

