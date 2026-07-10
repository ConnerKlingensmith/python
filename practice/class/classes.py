class PNC:
    def __init__(self,name,location):
        self.name = name
        self.location = location

emp1=PNC(input("Name: "), input("Location: ")) 
print(f"{emp1.name} is from {emp1.location}")

emp2=PNC("John", "Atlanta")
print(f"{emp2.name} is from {emp2.location}")


