from abc import ABC, abstractmethod

class Animal(ABC):
    """Abstract base class"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._species = "Unknown"
    
    @abstractmethod
    def make_sound(self):
        pass
    
    @abstractmethod
    def move(self):
        pass
    
    def sleep(self):
        print(f"{self.name} is sleeping... Zzz")
    
    def get_info(self):
        return f"{self.name} ({self._species}) is {self.age} years old"

class Cat(Animal):
    """
    Cat inherits from Animal
    MUST implement abstract methods
    """
    
    def __init__(self, name, age, indoor=True):
        # Call parent constructor
        super().__init__(name, age)
        self._species = "Feline"  # Set protected attribute
        self.__indoor = indoor    # Private attribute (name mangling)
    
    def make_sound(self):
        """Implement abstract method"""
        print(f"{self.name} says: Meow!")
    
    def move(self):
        """Implement abstract method"""
        print(f"{self.name} gracefully walks on silent paws")
    
    def purr(self):
        """Cat-specific method (not in Animal)"""
        print(f"{self.name} is purring... purrrr")
    
    def is_indoor(self):
        """Access private attribute via method"""
        return self.__indoor

# Create a Cat
cat = Cat("Whiskers", 3)

# Call inherited method
cat.sleep()

# Call implemented abstract methods
cat.make_sound()
cat.move()

# Call Cat-specific method
cat.purr()

# Call inherited get_info
print(cat.get_info())

# Check indoor status
print(f"Indoor cat: {cat.is_indoor()}")
