class Calculator:
    def addition(self, a, b):
        return a + b
    
    def subtraction(self, a, b):
        return a - b
    
    def multiplication(self, a, b):
        return a * b
    
    def division(self, a, b):
        return a / b
    
    def modulus(self, a, b):
        return a % b

obj = Calculator()

choice = input("What do you want to do?\n\n1) Addition\n2) Subtraction\n3) Multiplication\n4) Division\n5) Modulus(or Remainder)\n\n").lower().strip()

if choice == "addition":
    print(obj.addition(int(input("Enter the first number: ")), int(input("Enter the second number: "))))
elif choice == "subtraction":
    print(obj.subtraction(int(input("Enter the first number: ")), int(input("Enter the second number: "))))
elif choice == "multiplication":
    print(obj.multiplication(int(input("Enter the first number: ")), int(input("Enter the second number: "))))
elif choice == "division":
    print(obj.division(int(input("Enter the first number: ")), int(input("Enter the second number: "))))
elif choice == "modulus":
    print(obj.modulus(int(input("Enter the first number: ")), int(input("Enter the second number: "))))
else:
    print("Invalid choice!")