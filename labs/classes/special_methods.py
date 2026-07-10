class Animal:
    """Simple Animal without dunder methods"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Without __str__
animal = Animal("Buddy", 5)
print(animal)  # Ugly output!

print()

class BetterAnimal:
    """Animal with __str__ and __repr__"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        """
        Called by str() and print()
        Should be readable for end users
        """
        return f"{self.name} (age {self.age})"
    
    def __repr__(self):
        """
        Called by repr() and in REPL
        Should be unambiguous, ideally valid Python code
        """
        return f"BetterAnimal('{self.name}', {self.age})"

# With __str__ and __repr__
better = BetterAnimal("Max", 3)
print(better)           # Calls __str__
print(repr(better))     # Calls __repr__
print(f"Animal: {better}")  # Calls __str__

# In a list, __repr__ is used
animals = [better, BetterAnimal("Bella", 7)]
print(animals)
