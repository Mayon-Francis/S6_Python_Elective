import platform

print(platform.version())

n = int(input("Enter a number: "))

match n%2:
    case 0:
        print("Even")
    case 1:
        print("Odd")
    case _:
        print("Invalid")
