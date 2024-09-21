# Program to store strings in a list and print them

# Initialize an empty list to store strings
strings = []

# Loop to get input from the user
for _ in range(3):
    s = input("Enter a string: ")
    strings.append(s)

# Print all the strings in the list
print("Strings in the list:")
for string in strings:
    print(string)