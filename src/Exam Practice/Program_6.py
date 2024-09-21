class Bank:
    def __init__(self, Name, Amount, Account_Number):
        # Assign the input values to the instance variables
        self.Name = Name
        self.Amount = Amount
        self.Account_Number = Account_Number

    def Deposit(self, amt):
        self.Amount += amt

    def Withdrawal(self, amt):
        self.Amount -= amt
    
    def Minimum_Balance_Check(self):
        if self.Amount > 0:
            return True
        else:
            return False

    def Over_Draft(self, amt):
        self.Amount += amt

Name = input("Enter your name: ")
Amount = int(input("Enter your amount: "))
Account_Number = int(input("Enter your account number: "))

obj = Bank(Name, Amount, Account_Number)

for_deposit = int(input("Enter the amount you want to deposit: "))
obj.Deposit(for_deposit)

for_withdrawal = int(input("Enter the amount you want to withdraw: "))
obj.Withdrawal(for_withdrawal)

for_overdraft = int(input("Enter the amount you want to over-draft: "))
obj.Over_Draft(for_overdraft)

print("Name:", obj.Name)

if obj.Minimum_Balance_Check():
    print("Your current balance is:", obj.Amount)
else:
    print("Your current balance is:", obj.Amount, "(0)")

print(f"Name: {obj.Name}\nAmount: {obj.Amount}\nAccount Number: {obj.Account_Number}")