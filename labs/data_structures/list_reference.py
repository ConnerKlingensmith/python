list1 = [1, 2, 3]
list2 = list1

list2.append(4)

print(f"list1 = {list1}")
print(f"list2 = {list2}")

print(f"list1 is list2: {list1 is list2}") # is compares memory locations
print(f"id(list1) = {id(list1)}") # id prints memory location
print(f"id(list2) = {id(list2)}")
