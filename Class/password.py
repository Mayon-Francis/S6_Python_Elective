import getpass

username = input('Username: ')
password = getpass.getpass('Password: ')

# 1. Length
if(len(password) < 8):
    print("Password is too short")
    exit()

# 2. Upper Case
if(password.isupper()):
    print("Password must contain lower case characters")
    exit()

# 3. Lower Case
if(password.islower()):
    print("Password must contain upper case characters")
    exit()

# 4. Special Characters
if(password.isalnum()):
    print("Password must contain special characters")
    exit()

# 5. Numbers
if(password.isalpha()):
    print("Password must contain numbers")
    exit()

print("Password is strong")
