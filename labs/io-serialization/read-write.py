# Write to a file (overwrites if exists)
with open("network.txt", "w") as f:
    f.write("Router-1: 192.168.1.1\n")
    f.write("Router-2: 192.168.1.2\n")

# Append to a file
with open("network.txt", "a") as f:
    f.write("Router-3: 192.168.1.3\n")

# Write multiple lines at once
lines = [
    "Switch-1: 192.168.2.1\n",
    "Switch-2: 192.168.2.2\n",
]
with open("switches.txt", "w") as f:
    f.writelines(lines)

# Read entire file
with open("network.txt", "r") as f:
    content = f.read()
    print(content)

# Read line by line
with open("network.txt", "r") as f:
    for line in f:
        print(line.strip())  # strip() removes \n

# Read all lines into a list
with open("network.txt", "r") as f:
    lines = f.readlines()
    print(lines)
