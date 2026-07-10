# Dictionaries - same issue!
server1 = {"hostname": "web-01", "port": 8080}
server2 = server1  # Reference, not copy!

server2["port"] = 443

print(f"server1 = {server1}")  # Port changed to 443!
print(f"server2 = {server2}")

print()

# Solution: use .copy()
server3 = {"hostname": "db-01", "port": 5432}
server4 = server3.copy()

server4["port"] = 3306

print(f"server3 = {server3}")  # Port still 5432
print(f"server4 = {server4}")  # Port is 3306
