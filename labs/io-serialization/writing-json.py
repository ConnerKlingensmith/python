import json

# WRITING JSON
# Create a dictionary (configuration data)
network_config = {
    "hostname": "Router-1",
    "ip_address": "192.168.1.1",
    "interfaces": [
        {"name": "GigabitEthernet0/0", "ip": "10.0.0.1", "status": "up"},
        {"name": "GigabitEthernet0/1", "ip": "10.0.1.1", "status": "down"}
    ],
    "vlans": [10, 20, 30],
    "enabled": True
}

# Write to JSON file
with open("router_config.json", "w") as f:
    json.dump(network_config, f, indent=2)

# Convert to JSON string
json_string = json.dumps(network_config, indent=2)
print(json_string)

#READING JSON
# Read from JSON file
with open("router_config.json", "r") as f:
    config = json.load(f)

print(config["hostname"])
print(config["interfaces"][0]["name"])

# Parse JSON string
json_data = '{"device": "switch", "ports": 48}'
data = json.loads(json_data)
print(data["device"])

# Handle ERRORS
try:
    with open("config.json", "r") as f:
        data = json.load(f)
except FileNotFoundError:
    print("File not found")
except json.JSONDecodeError as e:
    print(f"Invalid JSON: {e}")
