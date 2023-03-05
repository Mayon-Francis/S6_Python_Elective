n = input("Enter a string: ")
vowels = 0
digits = 0
consonents = 0
spaces = 0
for c in n:
    if c in "aeiouAEIOU":
        vowels += 1
    elif c.isdigit():
        digits += 1
    elif c == " ":
        spaces += 1
    else:
        consonents += 1

print(f"Vowels: {vowels}")
print(f"Digits: {digits}")
print(f"Consonents: {consonents}")
print(f"Spaces: {spaces}")
