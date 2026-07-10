numbers = [1, 2, 3, 4, 5]
squares_dict = {x: x ** 2 for x in numbers}
print(f"Squares dict: {squares_dict}")

# Transform existing dictionary
devices = {
        "router1": "10.0.0.1",
        "router2": "10.0.0.2",
        "router3": "10.0.0.3"
}

# Swap keys and Values

ip_to_device = {ip: hostname for hostname, ip in devices.items()}
print(f"IP to device: {ip_to_device}")

# Filter Dictionary
routers_only = {name: ip for name, ip in devices.items() if name.startswith("router")}
print(f"Routers only: {routers_only}")

# Transform values

uppercase_devices = {name.upper(): ip for name, ip in devices.items()}
print(f"Uppercase names: {uppercase_devices}")
