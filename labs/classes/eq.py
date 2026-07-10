class Animal:
    """Animal without __eq__"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Without __eq__ - compares memory addresses
animal1 = Animal("Buddy", 5)
animal2 = Animal("Buddy", 5)

print(f"animal1 == animal2: {animal1 == animal2}")  # False - different objects
print(f"animal1 is animal2: {animal1 is animal2}")  # False

print()

class BetterAnimal:
    """Animal with __eq__"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __eq__(self, other):
        """
        Define what equality means
        Two animals are equal if name and age match
        """
        if not isinstance(other, BetterAnimal):
            return False
        return self.name == other.name and self.age == other.age
    
    def __str__(self):
        return f"{self.name} (age {self.age})"

# With __eq__ - compares attributes
better1 = BetterAnimal("Max", 3)
better2 = BetterAnimal("Max", 3)
better3 = BetterAnimal("Max", 5)

print(f"better1 == better2: {better1 == better2}")  # True - same name/age
print(f"better1 == better3: {better1 == better3}")  # False - different age
print(f"better1 is better2: {better1 is better2}")  # False - different objects
