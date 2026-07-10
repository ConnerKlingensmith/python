from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Abstract base class - cannot be instantiated directly
    Defines the contract for all animals
    """
    
    def __init__(self, name, age):
        """Constructor - called by subclasses"""
        self.name = name
        self.age = age
        self._species = "Unknown"  # Protected attribute (by convention)
    
    @abstractmethod
    def make_sound(self):
        """
        Abstract method - MUST be implemented by subclasses
        This method has no body here
        """
        pass
    
    @abstractmethod
    def move(self):
        """Another abstract method"""
        pass
    
    def sleep(self):
        """
        Concrete method - inherited by all subclasses
        Already has implementation
        """
        print(f"{self.name} is sleeping... Zzz")
    
    def get_info(self):
        """Concrete method using instance variables"""
        return f"{self.name} ({self._species}) is {self.age} years old"

# Try to create an Animal - this will FAIL!
try:
    animal = Animal("Generic", 5)
except TypeError as e:
    print(f"Cannot instantiate abstract class: {e}")
