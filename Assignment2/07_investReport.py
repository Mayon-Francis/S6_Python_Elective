startAmount = int(input("Enter the starting amount: "))
interestRate = float(input("Enter the interest rate: "))
years = int(input("Enter the number of years: "))


print(f"Year    Starting Balance    Interest   Ending Balance")
yearStartAmount=startAmount
for i in range(1, years+1):
    interest = yearStartAmount * interestRate / 100
    print(f"{i:<8}{yearStartAmount:<20}", end="")
    print(f"{interest:<11.2f}{yearStartAmount+interest:<15.2f}")
    yearStartAmount += interest

endAmount = yearStartAmount
print(f"Ending Balance: {endAmount:.2f}")
print(f"Total interest earned: {endAmount-startAmount:0.2f}")