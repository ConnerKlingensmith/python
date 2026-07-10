"""Q3) Create a class called Laptop.

   Attributes
   Brand
   RAM
   Processor
   
   Methods
   display_details()

   Create two Laptop objects and display their information."""

class Laptop:
    def __init__(self, brand, ram, processor):
        self.brand = brand
        self.ram = ram
        self.processor = processor

    def display_details(self):
        print(f"Brand: {self.brand}")
        print(f"RAM: {self.ram}")
        print(f"Processor: {self.processor}")
        print("-" * 25)

laptop1 = Laptop("HP", "16Gb", "Intel")
laptop2 = Laptop("Dell", "8Gb", "AMD")

laptop1.display_details()
laptop2.display_details()


