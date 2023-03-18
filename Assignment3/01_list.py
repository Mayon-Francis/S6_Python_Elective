stud = list()
stud =  stud + [44]
stud.append("Mayon Francis")
stud.extend(["piravom", 686664, 7034452171])
stud.insert(0, "MDL20CS073")

print("KTU_ID and Name: ", stud[0], stud[2])
print("Number of characters in name: ", len(stud[2]))
print("Last 5 digits of phone number: ", stud[5]%100000)
stud.reverse()
print("List reversed", stud)
print("Index of your name: ", stud.index("Mayon Francis"))
