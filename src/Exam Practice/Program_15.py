class details: # here both data abstraction and encapsulation is happening. 
    def __init__(self, name, age, income):
        self.name = name
        self.age = age
        self.income = income
        
    def printing_details(self):
        print(f"Name: {self.name}\nAge: {self.age}\nIncome: {self.income}")

obj = details(input("Enter your name: "), int(input("Enter your age: ")), int(input("Enter your income: ")))
obj.printing_details()