n = str(input("Enter n: "))
sum=0

print("The reverse is: ", n[::-1])
n = int(n)
while(n>0):
    sum+=n%10
    n=n//10
print("Sum of digits: ", sum)