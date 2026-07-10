import sys

# Generator expression - uses parentheses ()
gen_exp = (x ** 2 for x in range(10))

print(f"Generator expression: {gen_exp}")
print(f"Type: {type(gen_exp)}")
print(f"Memory: {sys.getsizeof(gen_exp)} bytes")

# It's a generator! Consumes values lazily
print(f"Values: {list(gen_exp)}")

print()

# List comprehension - uses square brackets []
list_comp = [x ** 2 for x in range(10)]

print(f"List comprehension: {list_comp}")
print(f"Type: {type(list_comp)}")
print(f"Memory: {sys.getsizeof(list_comp)} bytes")

print()
print("=" * 50)
print("THE TRUTH: List comprehension is just:")
print("  list( (x for x in range(10)) )")
print("It's a generator expression cast to a list!")
print("=" * 50)

print("====================================")

# Use generator expression when:
# - Processing large datasets
# - Values consumed once
# - Memory is constrained

# Sum of squares (no need to store list)
total = sum(x ** 2 for x in range(1000000))
print(f"Sum: {total}")

# Use list comprehension when:
# - Need to iterate multiple times
# - Need to index/slice
# - Dataset fits in memory

squares = [x ** 2 for x in range(10)]
print(f"First square: {squares[0]}")
print(f"Last square: {squares[-1]}")
print(f"Middle squares: {squares[3:7]}")
