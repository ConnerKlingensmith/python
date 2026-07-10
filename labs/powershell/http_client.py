import requests
import json

# Simple GET request
print("=== Get Public IP ===")
response = requests.get("https://api.ipify.org?format=json")
print(f"Status: {response.status_code}")
print(f"Your IP: {response.json()['ip']}")

# GET with inspection
print("\n=== GitHub API ===")
response = requests.get("https://api.github.com/users/github")
print(f"Status: {response.status_code}")
print(f"Content-Type: {response.headers['Content-Type']}")

data = response.json()
print(f"Name: {data['name']}")
print(f"Public repos: {data['public_repos']}")
