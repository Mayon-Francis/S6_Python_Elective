fileName = "test.temp.txt"
f = open(fileName, "w")
f.write("Hello\nhello2\nhello3")
f.close()

f2 = open(fileName, "r")
print("f2")
for line in f2:
    print(line)

f2.close()

f3 = open(fileName, "r")
print("f3")
print(f3.read())
f3.close()

f4 = open(fileName, "r")
print("f4")
while True:
    line = f4.readline()
    if not line:
        break
    print(line)
f4.close()

