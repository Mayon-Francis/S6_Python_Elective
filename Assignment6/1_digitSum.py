num = int(input("Enter a number: "))
sum = num%9
if sum == 0:
    sum = 9

print("The sum of digits is", sum)