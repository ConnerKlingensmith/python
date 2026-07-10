class Animal:
    """Animal with multiple dunder methods"""
    
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    
    def __str__(self):
        return f"{self.name} (age {self.age}, {self.weight}kg)"
    
    def __repr__(self):
        return f"Animal('{self.name}', {self.age}, {self.weight})"
    
    def __eq__(self, other):
        """Equality - same name, age, weight"""
        if not isinstance(other, Animal):
            return False
        return (self.name == other.name and 
                self.age == other.age and 
                self.weight == other.weight)
    
    def __lt__(self, other):
        """Less than - compare by weight"""
        if not isinstance(other, Animal):
            return NotImplemented
        return self.weight < other.weight
    
    def __len__(self):
        """Length - return age in months"""
        return self.age * 12
    
    def __bool__(self):
        """Truthiness - False if age is 0"""
        return self.age > 0
    
    def __add__(self, other):
        """Addition - combine weights (silly example)"""
        if not isinstance(other, Animal):
            return NotImplemented
        return self.weight + other.weight

# Create animals
cat = Animal("Whiskers", 3, 4.5)
dog = Animal("Buddy", 5, 25.0)
puppy = Animal("Newborn", 0, 2.0)

# __str__ and __repr__
print(cat)
print(repr(dog))

print()

# __eq__
cat2 = Animal("Whiskers", 3, 4.5)
print(f"cat == cat2: {cat == cat2}")
print(f"cat == dog: {cat == dog}")

print()

# __lt__ (enables sorting)
print(f"cat < dog: {cat < dog}")  # Compare by weight
animals = [dog, cat, puppy]
animals.sort()  # Uses __lt__
print(f"Sorted by weight: {animals}")

print()

# __len__
print(f"Cat age in months: {len(cat)}")
print(f"Dog age in months: {len(dog)}")

print()

# __bool__
if cat:
    print(f"{cat.name} is active (age > 0)")
if not puppy:
    print(f"{puppy.name} is newborn (age == 0)")

print()

# __add__
total_weight = cat + dog
print(f"Combined weight: {total_weight}kg")
