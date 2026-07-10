import psutil
import socket

# Get hostname
hostname = socket.gethostname()
print(f"Hostname: {hostname}")

# Get all network interfaces
print("\n=== Network Interfaces ===")
for interface, addrs in psutil.net_if_addrs().items():
    print(f"\n{interface}:")
    for addr in addrs:
        if addr.family == socket.AF_INET: #IPv4
            print(f" IPv4: {addr.address}")
            print(f" Netmask: {addr.netmask}")

# Get interface stats
print(f"\n === Interface Status ===")
stats = psutil.net_if_stats()
for interfaces, stat in stats.items():
    status = "Up" if stat.isup else "DOWN"
    print(f"{interface}: {status}, Speed: {stat.speed}Mbps")

#Get routing table
import subprocess
import re

print("\n=== Default Gateway ===")
result = subprocess.run(["route", "print", "0.0.0.0"], 
                       capture_output=True, text=True)
# Parse output (text processing)
for line in result.stdout.split('\n'):
    if '0.0.0.0' in line and 'On-link' not in line:
        parts = line.split()
        if len(parts) >= 3:
            print(f"Gateway: {parts[2]}")
            break
