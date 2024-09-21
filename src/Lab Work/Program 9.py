# Program with a class definition and calling a print function

# Class definition
class MyClass:
    def __init__(self, message):
        self.message = message  # Initialize the message attribute
    
    # Method to print the message
    def print_message(self):
        print(self.message)

# Create an object of MyClass
obj = MyClass("Hello from MyClass!")

# Call the print_message method
obj.print_message()