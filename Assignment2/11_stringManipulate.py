# Initializing the string
str = "Python Programming by Mayon"

# a) To display the last four characters.
print("Last four characters:", str[-4:])
# b) To display the substring starting from index 4 and ending at index 8.
print("Substring from index 4 to 8:", str[4:9])
# c) Find the length of the string, min and max(characters)
print("Length of the string:", len(str))
print("Minimum character:", min(str))
print("Maximum character:", max(str))
# d) To trim the last four characters from the string.
trimmed_str = str[:-4]
print("String after trimming last four characters:", trimmed_str)
# e) To trim the first four characters from the string.
trimmed_str = str[4:]
print("String after trimming first four characters:", trimmed_str)
# f) To display the starting index of the substring 'gr'.
print("Starting index of the substring 'gr':", str.index("gr"))
# g) To change the case of the given string.( small letter to capital and capital to small)
print("String in swapped case:", str.swapcase())
# h) To check if the string is in title case.
print("Is the string in title case?", str.istitle())
# i) To replace all the occurrences of letter 'm' in the string with '*'
new_str = str.replace('m', '*')
print("String after replacing 'm' with '*':", new_str)
# j) Reverse the string
reversed_str = str[::-1]
print("Reversed string:", reversed_str)
# k) Count the occurrence of the character ‘m’
m_count = str.count('m')
print("Number of occurrences of 'm':", m_count)
# l) Characters in even positions 0,2,4,…
print("Characters in even positions:", str[::2])
# m) Characters in even positions 0,2,4,… in reverse order
print("Characters in even positions in reverse order:", str[::-2])
# n) Check whether the substring ‘on’ is present in the string or not
print("Is 'on' present in the string?", 'on' in str)
# o) Find the first occurrence of character ‘t’
print("Index of first occurrence of 't':", str.index('t'))
# p) Convert the string into upper case
print("Uppercase string:", str.upper())
