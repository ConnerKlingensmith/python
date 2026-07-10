list1 = [1, 2, 3]
list2 = list1.copy()

list2.append(4)

print(f"list1 = {list1}")  # [1, 2, 3] - unchanged!
print(f"list2 = {list2}")  # [1, 2, 3, 4]
print(f"list1 is list2: {list1 is list2}")

print()

list3 = [10, 20, 30]
list4 = list(list3)
list4.append(40)

print(f"list3 = {list3}")
print(f"list3 = {list4}")

print()

list5 = [100, 200, 300]
list6 = list5[:]

list6.append(400)

print(f"list5 = {list5}")  # [100, 200, 300]
print(f"list6 = {list6}")
