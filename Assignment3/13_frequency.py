print("Enter 10 numbers: ")
numList = []
for i in range(10):
    numList.append(int(input("> ")))

numList.sort()

maxCount = 0
maxNum = set()
for i in range(len(numList)):
    count = 0
    for j in range(len(numList)):
        if numList[i] == numList[j]:
            count += 1
    if count > maxCount:
        maxCount = count
        maxNm = {numList[i]}
    elif count == maxCount:
        maxNm.add(numList[i])

print("Numbers with largest frequency of occurrence: ", maxNm)