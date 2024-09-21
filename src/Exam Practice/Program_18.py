my_list = [10, 20, 30, 40, 50]

print(my_list)
my_list.append(60)
print("After append:", my_list)

my_list.insert(2, 25)
print("After insert:", my_list)

my_list.remove(40)
print("After remove:", my_list)

popped_element = my_list.pop()
print("After pop:", my_list, "| Popped element:", popped_element)

my_list.sort()
print("After sort:", my_list)






my_tuple = (5, 10, 15, 20, 25)

element = my_tuple[2]
print("Element at index 2:", element)

count_15 = my_tuple.count(15)
print("Count of 15:", count_15)

index_20 = my_tuple.index(20)
print("Index of 20:", index_20)

sliced_tuple = my_tuple[1:4]
print("Sliced tuple:", sliced_tuple)

new_tuple = my_tuple + (30, 35, 40)
print("Concatenated tuple:", new_tuple)






my_dict = {"name": "John", "age": 30, "city": "New York"}

my_dict["profession"] = "Engineer"
print("After adding new key-value pair:", my_dict)

my_dict["age"] = 31
print("After updating 'age':", my_dict)

removed_value = my_dict.pop("city")
print("After pop:", my_dict, "| Removed value:", removed_value)

profession = my_dict.get("profession")
print("Profession:", profession)

keys = my_dict.keys()
values = my_dict.values()
print("Keys:", list(keys), "| Values:", list(values))