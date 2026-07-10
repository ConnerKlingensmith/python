class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says: woof!")

    def get_info(self):
        return f"{self.name} is {self.age} years old"

dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

# call methods

dog1.bark()
dog2.bark()

print(dog1.get_info())
print(dog2.get_info())

# Access atributes directly

print(f"\nDirect access: {dog1.name}, {dog2.name}")

