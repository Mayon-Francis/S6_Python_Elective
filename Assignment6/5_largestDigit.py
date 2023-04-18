num = input("Enter a number: ")
temp = int(num)
largest = 0
while temp > 0:
    digit = temp%10
    if digit > largest:
        largest = digit
    temp = temp//10

index = num.index(str(largest)) + 1
print(f"The largest digit is {largest} at position {index}")