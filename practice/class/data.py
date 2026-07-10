class Animal:
    def speak(self):
        return "The animal can speak"

class Dog(Animal):
    def speak(self):
        return "bark"


a1 = Animal()
print(a1.speak())

a2 = Dog()
print(a2.speak())

