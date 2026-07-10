import socket
import subprocess
import platform

def ping(host, count=4):
    """Ping a host - works cross-platform"""
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, str(count), host]
    
    result = subprocess.run(command, capture_output=True, text=True)
    return result.returncode == 0

def test_port(host, port, timeout=3):
    """Test if a TCP port is open"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    
    try:
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except socket.gaierror:
        return False

# Test ping
print("=== Ping Test ===")
hosts = ["8.8.8.8", "google.com", "192.168.1.1"]
for host in hosts:
    status = "✓ UP" if ping(host, 2) else "✗ DOWN"
    print(f"{host}: {status}")

# Test ports
print("\n=== Port Test ===")
test_cases = [
    ("google.com", 443, "HTTPS"),
    ("google.com", 80, "HTTP"),
]

for host, port, service in test_cases:
    status = "✓ OPEN" if test_port(host, port) else "✗ CLOSED"
    print(f"{host}:{port} ({service}): {status}")
