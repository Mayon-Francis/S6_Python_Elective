print("Enter 5 numbers: ")
numList = []
for i in range(5):
    numList.append(int(input("> ")))

ascNumList = sorted(numList)
descNumList = sorted(numList, reverse=True)

if numList == ascNumList:
    print("Ascending")
elif numList == descNumList:
    print("Descending")
else:
    print("Unsorted")