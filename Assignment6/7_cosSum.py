import math
n = int(input("Enter n: "))
x = int(input("Enter x: "))
sum=0
print("Series: ", end=" ")
for i in range(0, n+1, 2):
    temp = 1
    if(i == 1):
        pass
    elif i % 4 == 1:
        print("+", end=" ")
    else:
        temp *= -1
        print("-", end=" ")
    if i ==1:
        print("x", end=" ")
    else:
        print("x^{}/{}!".format(i,i), end=" ")
    temp *= (x**i)/math.factorial(i)
    sum += temp
print()
print("Sum: {}\n".format(sum))