# Program to verify user input and print welcome

# Input: User's name
user_input = input("Enter your name: ")

# Check if the input is alphabetic
if user_input.isalpha():
    print(f"Welcome, {user_input}!")
else:
    print("Invalid input! Please enter a valid name.")