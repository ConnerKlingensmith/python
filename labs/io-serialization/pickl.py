import pickle

# Create complex Python objects
network_devices = [
    {"hostname": "Router-1", "ip": "192.168.1.1", "ports": [1, 2, 3]},
    {"hostname": "Switch-1", "ip": "192.168.2.1", "ports": [10, 20, 30]},
]

# Save to pickle file (binary)
with open("devices.pkl", "wb") as f:
    pickle.dump(network_devices, f)

# Can pickle almost any Python object
class Router:
    def __init__(self, name, ip):
        self.name = name
        self.ip = ip

router = Router("Router-1", "192.168.1.1")

with open("router.pkl", "wb") as f:
    pickle.dump(router, f)

# Unpickling Objects
# Load from pickle file
with open("devices.pkl", "rb") as f:
    devices = pickle.load(f)

print(devices[0]["hostname"])

# Load custom object
with open("router.pkl", "rb") as f:
    router = pickle.load(f)

print(f"{router.name}: {router.ip}")
