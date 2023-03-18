l = [1, 1.0, 2, "Hi", "Hello", 3.14, 9.18]
intL = []
floatL = []
strL = []
for i in l:
    if type(i) == int:
        intL.append(i)
    elif type(i) == float:
        floatL.append(i)
    elif type(i) == str:
        strL.append(i)

print("Integer List: ", intL)
print("Float List: ", floatL)
print("String List: ", strL)
