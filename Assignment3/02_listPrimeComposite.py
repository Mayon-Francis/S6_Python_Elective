l = list()
prime = list()
composite = list()
n = int(input("Enter the number of elements: "))
def isPrime(n):
    if n > 1:
        for i in range(2, n//2 + 1):
            if (n % i) == 0:
                return False
        return True
    else:
        return False
    
for i in range(0, n):
    ele = int(input(f"Enter element {i+1}:"))
    l.append(ele)
    if isPrime(ele):
        prime.append(ele)
    else:
        composite.append(ele)
print("List: ", l)
print("Prime: ", prime)
print("Composite: ", composite)
