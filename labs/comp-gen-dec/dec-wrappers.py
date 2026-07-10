def simple_function():
    """A simple function"""
    return "Hello!"

def uppercase_decorator(func):
    """
    Decorator that makes function return uppercase
    Takes a function, returns a new function
    """
    def wrapper():
        # Call original function
        result = func()
        # Modify result
        return result.upper()
    
    return wrapper

# Manual decoration
original = simple_function
decorated = uppercase_decorator(original)

print(f"Original: {original()}")
print(f"Decorated: {decorated()}")

print()
print("=" * 50)
print("DECORATORS ARE JUST FUNCTION WRAPPERS!")
print("decorated = uppercase_decorator(original)")
print("=" * 50)
