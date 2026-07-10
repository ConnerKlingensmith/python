# The old way (verbose)
squares = []
for x in range(10):
    squares.append(x ** 2)

print(f"Old way: {squares}")

# The comprehension way (concise)
squares = [x ** 2 for x in range(10)]
print(f"Comprehension: {squares}")

# With filtering
evens = [x for x in range(20) if x % 2 == 0]
print(f"Even numbers: {evens}")

# With transformation and filtering
even_squares = [x ** 2 for x in range(20) if x % 2 == 0]
print(f"Squares of evens: {even_squares}")
