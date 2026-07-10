"""Q1 : Write a Python program that:
Creates a dictionary with the following details:

Hostname : Router01
IP : 192.168.1.1
Vendor : Cisco

Save the dictionary into a file called device.json.
Read the same file.
Print the contents."""

import json

device = {
        "hostname": "Router01",
        "IP": "192.168.1.1",
        "Vendor": "Cisco"
}

with open("device.json", "w") as file:
    json.dump(device, file, indent=4)

with open("device.json", "r") as file:
    data = json.load(file)

print(data)

