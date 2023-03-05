import math

n = str(input("Enter a number: "))
sum = 0
for d in n:
    sum += math.factorial(int(d))

if sum == int(n):
    print(f"{n} is a Krishnamurthy number.")
else:
    print(f"{n} is not a Krishnamurthy number.")