n = input("Enter a two digit hex number: ")

def hexToDec(hex):
    if hex == "0":
        return 0
    elif hex == "1":
        return 1
    elif hex == "2":
        return 2
    elif hex == "3":
        return 3
    elif hex == "4":
        return 4
    elif hex == "5":
        return 5
    elif hex == "6":
        return 6
    elif hex == "7":
        return 7
    elif hex == "8":
        return 8
    elif hex == "9":
        return 9
    elif hex == "A":
        return 10
    elif hex == "B":
        return 11
    elif hex == "C":
        return 12
    elif hex == "D":
        return 13
    elif hex == "E":
        return 14
    elif hex == "F":
        return 15
    
decimal = hexToDec(n[0]) * 16 + hexToDec(n[1])
binary = ""
print(f"Decimal of {n} is {decimal}")
while decimal > 0:
    binary = str(decimal % 2) + binary
    decimal = decimal // 2
print(f"Binary of {n} is {binary}")