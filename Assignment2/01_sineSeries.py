n = int(input("Enter n: "))

for i in range(1, n+1, 2):
    if(i == 1):
        pass
    elif i % 4 == 1:
        print("+", end=" ")
    else:
        print("-", end=" ")

    if i ==1:
        print("x", end=" ")
    else:
        print("x^{}/{}!".format(i,i), end=" ")

print("\n")