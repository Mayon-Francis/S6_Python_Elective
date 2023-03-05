def numToDigitWord(num):
    if num == 1:
        return "One"
    elif num == 2:
        return "Two"
    elif num == 3:
        return "Three"
    elif num == 4:
        return "Four"
    elif num == 5:
        return "Five"
    elif num == 6:
        return "Six"
    elif num == 7:
        return "Seven"
    elif num == 8:
        return "Eight"
    elif num == 9:
        return "Nine"
    elif num == 0:
        return "Zero"
    else:
        return "Invalid Number"

n = input("Enter a number: ")

for d in n:
    print(numToDigitWord(int(d)), end=" ")

print()