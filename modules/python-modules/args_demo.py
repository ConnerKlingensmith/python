# *args - variable positional arguments (becomes tuple)
def add_all(*args):
    """Add any number of arguments"""
    return sum(args)

print(f"add_all(1, 2, 3): {add_all(1, 2, 3)}")
print(f"add_all(10, 20, 30, 40): {add_all(10, 20, 30, 40)}")

# **kwargs - variable keyword arguments (becomes dict)
def greet(name, **kwargs):
    """Greet with options"""
    greeting = kwargs.get("greeting", "Hello")
    punctuation = kwargs.get("punctuation", "!")
    return f"{greeting}, {name}{punctuation}"

print(f"greet('Alice'): {greet('Alice')}")
print(f"greet('Bob', greeting='Hi', punctuation='!!!'): {greet('Bob', greeting='Hi', punctuation='!!!')}")

# Unpacking in assignments
numbers = [1, 2, 3, 4, 5]
a, b, *rest = numbers
print(f"\na, b, *rest = {numbers}")
print(f"a={a}, b={b}, rest={rest}")

# Unpacking in function calls
values = [10, 20, 30]
print(f"\nadd_all(*{values}) = {add_all(*values)}")

# Merging dicts with unpacking
defaults = {"host": "localhost", "port": 8080}
overrides = {"port": 443}
config = {**defaults, **overrides}
print(f"\nMerged config: {config}")
