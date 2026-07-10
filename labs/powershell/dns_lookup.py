import socket

# Basic lookup (name to IP)
def lookup_host(hostname):
    """Get IP address from hostname"""
    try:
        ip = socket.gethostbyname(hostname)
        return ip
    except socket.gaierror:
        return None

# Reverse lookup (IP to name)
def reverse_lookup(ip):
    """Get hostname from IP"""
    try:
        hostname = socket.gethostbyaddr(ip)[0]
        return hostname
    except socket.herror:
        return None

# Test lookups
print("=== DNS Lookups ===")
hosts = ["google.com", "github.com", "cloudflare.com"]

for host in hosts:
    ip = lookup_host(host)
    print(f"{host} -> {ip}")

print("\n=== Reverse Lookups ===")
ips = ["8.8.8.8", "1.1.1.1"]

for ip in ips:
    hostname = reverse_lookup(ip)
    print(f"{ip} -> {hostname}")

# For advanced DNS queries, use dnspython library
print("\n=== Advanced DNS (requires: pip install dnspython) ===")
try:
    import dns.resolver
    
    # Get A records
    answers = dns.resolver.resolve('google.com', 'A')
    print("\nA records for google.com:")
    for rdata in answers:
        print(f"  {rdata}")
    
    # Get MX records
    answers = dns.resolver.resolve('google.com', 'MX')
    print("\nMX records for google.com:")
    for rdata in answers:
        print(f"  {rdata.preference} {rdata.exchange}")
        
except ImportError:
    print("Install dnspython for advanced DNS: pip install dnspython")
except Exception as e:
    print(f"DNS query failed: {e}")
