stud = dict()

stud[44] = "Mayon"
stud[45] = "Rohit"
stud[46] = "Raj"
stud[47] = "Ravi"
stud[48] = "Rajesh"

print(stud)
print(list(stud.keys()))
print(list(stud.values()))

stud1 = {
    44: ("Mayon", 20),
    45: ("Rohit", 21), 
    46: ("Raj", 22),
    47: ("Ravi", 23),
    48: ("Rajesh", 24)
}

print(stud1)
details = list(stud1.values())
details.sort(key=lambda x: x[1], reverse=True)
print(details[0] )

rNo = int(input("Enter roll no: "))
del stud1[rNo]
print(stud)

print("Passed students: ")
for key, value in stud1.items():
    if value[1] >= 20:
        print(key, value)