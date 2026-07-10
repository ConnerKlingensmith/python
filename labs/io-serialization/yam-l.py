import yaml

# Writing YAML
# Same dictionary as before
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

# Write to YAML file
with open("router_config.yaml", "w") as f:
    yaml.dump(network_config, f, default_flow_style=False)

# Convert to YAML string
yaml_string = yaml.dump(network_config, default_flow_style=False)
print(yaml_string)

# Reading YAML
with open("router_config.yaml", "r") as f:
    config = yaml.safe_load(f)

print(config["hostname"])
print(config["interfaces"][0]["name"])

    # safe_load() is safer than load() - prevents code execution

