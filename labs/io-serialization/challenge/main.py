import csv
import json
import yaml
import pickle
from dotenv import load_dotenv
import os

# Load ENV
load_dotenv()

username = os.getenv("DEVICE_USERNAME")
password = os.getenv("DEVICE_PASSWORD")
ssh_port = os.getenv("SSH_PORT")


# Read CSV
devices = []
with open("devices.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        devices.append(row)

print(devices)

# JSON Format

with open("inventory.json", "w") as file:
    json.dump(devices, file, indent=4)


# YAML Format

with open("inventory.yaml", "w") as file:
    yaml.dump(devices, file)

# Pickle Format

with open("inventory.pkl", "wb") as file:
    pickle.dump(devices, file)

# Load JSON

with open("inventory.json", "r") as file:
    json_data = json.load(file)

# Load YAML

with open("inventory.yaml") as file:
    yaml_data = yaml.safe_load(file)

# Load Pickle

with open("inventory.pkl", "rb") as file:
    pickle_data = pickle.load(file)


# -----------------------------
# Verify
# -----------------------------
if json_data == yaml_data == pickle_data:
    print("\nAll inventories contain identical data.")
else:
    print("\nInventory mismatch!")
