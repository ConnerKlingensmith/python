import json

server = {
        "hostname": "webserver1",
        "ip": "192.168.1.1"
}

with open("server", "w") as file:
    json.dump(server,file)

with open("server", "r") as file:
    data = json.load(file)
    
print(data["hostname"])
