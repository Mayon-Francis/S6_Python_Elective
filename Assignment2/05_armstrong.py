num = int(input("Enter a number: "))
order = len(str(num))
sum = 0
for digit in str(num):
    sum += int(digit) ** order
    
if sum == num:
    print("{} is armstrong".format(num))
else:
    print("{} is not armstrong".format(num))