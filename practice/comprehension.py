numbers = [3, 7, 12, 18, 5, 22]
result = []

for n in numbers:
    if n < 10:
        result.append(n)

sqr = [n*n for n in numbers]

print(result)
print(sqr)

