string = input("Enter a string to check if it is a palindrome or not: ")
if string == string[::-1]:
    print("The entered string is palindrome.")
else:
    print("The entered string is not a palindrome.")