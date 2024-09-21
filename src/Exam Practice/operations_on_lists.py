list_1 = []

list_1 = list(map(int, input("Enter the numbers of the list:\n").split()))

num = int(input("Enter the number that you want to insert: "))
index = int(input(f"Enter the index number at which you want to insert {num}: "))

list_1.insert(index, num)

print(list_1)

rem = int(input("Enter the number whose first occurrence you want to delete from the list: "))

if rem in list_1:
    list_1.remove(rem)

apnd = int(input("Enter the number which you want to append into the list: ")) 

list_1.append(apnd)

list_1.pop()

list_1.reverse()

print(list_1)