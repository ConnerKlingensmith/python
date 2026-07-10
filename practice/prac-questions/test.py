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


# Create two Laptop objects
laptop1 = Laptop("Dell", "16 GB", "Intel Core i7")
laptop2 = Laptop("HP", "8 GB", "AMD Ryzen 5")

# Display information
laptop1.display_details()
laptop2.display_details()
