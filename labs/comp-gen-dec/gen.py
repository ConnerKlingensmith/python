import sys

def generate_primes_list(n):
    """Generate primes up to n - returns a LIST (memory intensive)"""
    primes = []

    for i in range(2, n + 1):
        is_prime = False
        for p in range(2, int(i ** 0.5) + 1):
            if i % p == 0:
                break
        else: # else on a for runs only if the loop is never broken
            is_prime = True
        if is_prime:
            primes.append(i)

    return primes

def generate_primes_generator(n):
    """Generate primes up to n - YIELDS values (memory efficient)"""

    for i in range(2, n + 1):
        is_prime = True
        for p in range(2, int(i ** 0.5) + 1):
            if i % p == 0:
                is_prime = False
                break
        if is_prime:
            yield i  # Key difference - yield instead of storing!

# Compare memory usage
print("=" * 50)
print("MEMORY COMPARISON")
print("=" * 50)

# List version - stores ALL primes in memory
primes_list = generate_primes_list(10000)
list_size = sys.getsizeof(primes_list)
print(f"List of 10,000 primes: {list_size:,} bytes")

# Generator version - stores only the generator object
primes_gen = generate_primes_generator(10000)
gen_size = sys.getsizeof(primes_gen)
print(f"Generator object: {gen_size:,} bytes")

print(f"\nMemory savings: {list_size / gen_size:.1f}x smaller!")

# Generators are consumed on-the-fly
print("\n" + "=" * 50)
print("USING THE GENERATOR")
print("=" * 50)

# Get first 10 primes
primes_gen = generate_primes_generator(10)
first_10 = list(primes_gen)  # Convert to list to see them
print(f"First 10 primes: {first_10}")

# Or iterate without converting
print("\nFirst 20 primes (one at a time):")
for i, prime in enumerate(generate_primes_generator(20), 1):
    print(f"{i}. {prime}")

# STEP 2

def simple_generator():
    """Demonstrates how yield works"""
    print("Starting...")
    yield 1
    print("Between yields...")
    yield 2
    print("Almost done...")
    yield 3
    print("Generator exhausted!")

# Create generator
gen = simple_generator()
print(f"Generator created: {gen}")
print(f"Type: {type(gen)}")

# Each next() call runs until the next yield
print("\nCalling next():")
print(f"First: {next(gen)}")
print(f"Second: {next(gen)}")
print(f"Third: {next(gen)}")

# Try to get another - generator is exhausted!
try:
    print(f"Fourth: {next(gen)}")
except StopIteration:
    print("StopIteration raised - no more values!")
