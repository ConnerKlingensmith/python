import yaml

server = {
        "hostname": "DBserver",
        "ip": "10.0.1.1"
}

with open("server", "w") as file:
    yaml.dump(server,file)

with open("server", "r") as file:
    data = yaml.safe_load(file)
    
print(data)
