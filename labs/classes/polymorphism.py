from abc import ABC, abstractmethod

class Animal(ABC):
    """Abstract base class"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._species = "Unknown"
    
    @abstractmethod
    def make_sound(self):
        """Every animal must make a sound"""
        pass
    
    @abstractmethod
    def move(self):
        """Every animal must be able to move"""
        pass
    
    def sleep(self):
        """Common behavior - inherited by all"""
        print(f"{self.name} is sleeping... Zzz")
    
    def get_info(self):
        return f"{self.name} ({self._species}) is {self.age} years old"

class Cat(Animal):
    """Cat implementation"""
    
    def __init__(self, name, age, indoor=True):
        super().__init__(name, age)
        self._species = "Feline"
        self.__indoor = indoor
    
    def make_sound(self):
        print(f"{self.name} says: Meow!")
    
    def move(self):
        print(f"{self.name} gracefully walks")
    
    def purr(self):
        print(f"{self.name} is purring...")

class Dog(Animal):
    """Dog implementation"""
    
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self._species = "Canine"
        self.__breed = breed
    
    def make_sound(self):
        print(f"{self.name} says: Woof!")
    
    def move(self):
        print(f"{self.name} runs energetically")
    
    def fetch(self):
        print(f"{self.name} fetches the ball!")

# Polymorphic function - works with ANY Animal
def animal_action(animal):
    """
    Takes any Animal and calls its methods
    Polymorphism - same interface, different behavior
    """
    # Type checking
    if not isinstance(animal, Animal):
        print(f"Error: {animal} is not an Animal!")
        return
    
    print(f"\n--- {animal.name} ---")
    print(animal.get_info())
    animal.make_sound()  # Polymorphic call - behavior depends on type
    animal.move()        # Polymorphic call
    animal.sleep()       # Inherited method

# Create animals
cat = Cat("Whiskers", 3)
dog = Dog("Buddy", 5, "Golden Retriever")

# Polymorphism - same function, different behavior
animal_action(cat)
animal_action(dog)

# Type checking with isinstance
print(f"\nIs cat an Animal? {isinstance(cat, Animal)}")
print(f"Is cat a Cat? {isinstance(cat, Cat)}")
print(f"Is cat a Dog? {isinstance(cat, Dog)}")

# Try with a non-Animal
animal_action("Not an animal")
