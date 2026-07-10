# Flatten a matrix (2D list to 1D list)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# The verbose way
flattened = []
for row in matrix:
    for num in row:
        flattened.append(num)

print(f"Flattened (verbose): {flattened}")

# The comprehension way
flattened = [num for row in matrix for num in row]
print(f"Flattened (comprehension): {flattened}")

# Read it as: "for each row in matrix, for each num in that row"

# With filtering
even_only = [num for row in matrix for num in row if num % 2 == 0]
print(f"Even numbers only: {even_only}")

# Create multiplication table
mult_table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
print("\nMultiplication table:")
for row in mult_table:
    print(row)
