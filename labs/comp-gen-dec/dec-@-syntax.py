# The @ syntax is just sugar for the pattern above

def uppercase_decorator(func):
    """Uppercase decorator"""
    def wrapper():
        return func().upper()
    return wrapper

# Using @ syntax
@uppercase_decorator
def greet():
    """Greet someone"""
    return "hello, world!"

# This is EXACTLY the same as:
# def greet():
#     return "hello, world!"
# greet = uppercase_decorator(greet)

print(f"Result: {greet()}")

# Multiple decorators stack
def exclamation_decorator(func):
    """Add exclamation marks"""
    def wrapper():
        return func() + "!!!"
    return wrapper

@exclamation_decorator
@uppercase_decorator
def shout():
    return "python is awesome"

# Order matters! Read bottom-to-top:
# 1. uppercase_decorator wraps shout
# 2. exclamation_decorator wraps the result

print(f"Shouting: {shout()}")
