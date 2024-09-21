import random

def check_password(password):
    count = 0
    special_characters = "!@#$%^&*()-+"
    if len(password) >= 6:
         count += 1
    else:
        less_letters = 6 - len(password)
        password += ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=less_letters))
    if any(char.isdigit() for char in password):
        count += 1
    else:
        password += random.choice("1234567890")

    if any(char.islower() for char in password):
        count += 1
    else:
        password += random.choice("abcdefghijklmnopqrstuvwxyz")

    if any(char.isupper() for char in password):
        count += 1
    else:
        password += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    
    if any(char in special_characters for char in password):
        count += 1
    else:
        password += random.choice(special_characters)
    
    if count == 5:
        print("The password is good enough!!")
    else:
        print("The new password is:", password)

check_password(input("Enter the password: "))