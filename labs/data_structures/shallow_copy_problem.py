list1 = [[1, 2], [3, 4]]
list2 = list1.copy()

list2[0].append(999)

print(f"list1 = {list1}")
print(f"list2 = {list2}")

print(f"list1 is list2: {list1 is list2}")
print(f"list1[0] is list2[0]: {list1[0] is list2[0]}")
