print("Enter 5 strings: ")
strList = []
for i in range(5):
    s = input("> ")
    strList.append(s)

totalCharLen = 0
for str in strList:
    print(f"String: {str}, length: {len(str)}")
    totalCharLen += len(str)

print(f"Average string length: {totalCharLen/len(strList)}")

