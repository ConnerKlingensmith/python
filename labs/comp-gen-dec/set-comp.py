
# Transform and deduplicate
words = ["hello", "world", "hello", "python"]
uppercase_unique = {word.upper() for word in words}
print(f"Unique uppercase: {uppercase_unique}")

# Extract unique values from nested structure
devices = [
    {"hostname": "router1", "location": "us-east"},
    {"hostname": "switch1", "location": "us-west"},
    {"hostname": "router2", "location": "us-east"},
]

locations = {device["location"] for device in devices}
print(f"Unique locations: {locations}")
