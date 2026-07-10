import socket

def safe_tcp_client(host, port):
    """TCP client with error handling"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)  # 5 second timeout
        
        sock.connect((host, port))
        sock.send(b"Hello")
        
        data = sock.recv(1024)
        print(f"Received: {data.decode()}")
        
        sock.close()
        
    except socket.timeout:
        print("Connection timed out")
    except ConnectionRefusedError:
        print("Connection refused - is server running?")
    except socket.gaierror:
        print("Invalid hostname")
    except Exception as e:
        print(f"Error: {e}")

# Test it
safe_tcp_client("127.0.0.1", 8080)
