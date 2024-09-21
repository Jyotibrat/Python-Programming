T = int(input("Enter the number of test cases: "))
for i in range(T):
    try:
        list_for_division = list(map(int, input("Enter the numbers for the division: ").split()))
        
        if len(list_for_division) % 2 != 0:
            raise ValueError("The number of inputs must be even, as we are dividing pairs of numbers.")
        
        for i in range(0, len(list_for_division), 2):
            a, b = list_for_division[i], list_for_division[i + 1]
            try:
                quotient = a / b
                remainder = a % b
                print(f"Quotient: {quotient}, Remainder: {remainder}")
            except ZeroDivisionError:
                print("Error: Division by zero is not allowed.")
    except ValueError as ve:
        print(f"ValueError: {ve}. Please enter valid integer pairs.")