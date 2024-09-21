set_1 = {1, 2, 3}
set_2 = {3, 4, 5}

#returns only those elements in set 1 which are not in set 2.
diff = set_1.difference(set_2)
print(diff)

#returns the result in boolean and checks that if set 1 is fully inside set 2 or not.
print(set_1.issubset(set_2))

#returns the result in boolean and checks if any elements are common in between set 1 and set 2.
print(set_1.isdisjoint(set_2))

#returns all the elements of set 1 and set 2 which are not common in between.
print(set_1.symmetric_difference(set_2))

#printing the set 1 and set 2.
print(set_1)
print(set_2)

#printing the set 1 after clearing all the elements which were inside the set 1.
empty_set_1 = set_1.clear()
print(empty_set_1)

#copying and printing the set 2.
copied_set_2 = set_2.copy()
print(copied_set_2)