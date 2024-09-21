odd = []
even = []
for _ in range(101, 201):
    if _ % 2 == 0:
        even.append(_)
    else:
        odd.append(_)

print(f"The list of even numbers between 101 and 200 is {even}\nThe list of odd numbers between 101 and 200 is {odd}") 