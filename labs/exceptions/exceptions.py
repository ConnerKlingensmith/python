#age = int(input("Enter your age: "))
#print(f"You are {age} years old")

# Handle the error gracefully
"""
while True:
    try:
        age = int(input("Enter your age: "))
        print(f"You are {age} years old")
        break
    except:
        print("That's not a valid age!")
        continue
"""
"""
try:
    age = int(input("Enter your age: "))
    print(f"You are {age} years old")
except ValueError as e:
    print(f"Invalid input: {e}")
"""

"""
def get_number():
    try: 
        num = int(input("Enter a number: "))
        return num
    except ValueError:
        print("That's not a valid number!")
        return None

result = get_number()
if result is not None:
    print(f"Your entered: {result}")
"""

# Dictionary Key Not Found
"""
device_config = {
        "hostname": "router-1",
        "ip": "192.168.1.1",
        "port": 22
}

    # Bad Approach - crashes if key missing --> device_config["username"]
    # BETTER APPROACH -- Use .get with default value --> device_config.get("username", "admin")

try:
    username = device_config.get("username", "admin")
except KeyError:
    print("Username not found in config")
    username = "admin"  # Use default

print(f"Username: {username}")
"""

# File Not Found Error -- File Doesn't Exist

try:
    with open("config.txt", "r") as f:
        data = f.read()
        print(data)
except FileNotFoundError:
    print("Config file not found, using defaults")
    data = "default config"

# Zero Division Error
def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        return None

print(safe_divide(10, 2))   # 5.0
print(safe_divide(10, 0))   # Cannot divide by zero! / None
