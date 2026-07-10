import socket

# Create TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 8000

server_socket.bind((HOST, PORT))
server_socket.listen(5)
print(f"HTTP Server running on http://{HOST}:{PORT}")
print("Open your browser and visit the URL above")
print("Press Ctrl+C to stop")

# Request counter
request_count = 0

# Keep server running
while True:
    # Accept connection
    client_socket, client_address = server_socket.accept()
    request_count += 1
    print(f"\nRequest #{request_count} from {client_address}")
    
    # Receive HTTP request
    request = client_socket.recv(1024).decode()
    print("Request received:")
    print(request.split('\r\n')[0])  # Print just the request line
    
    # Send HTTP response
    http_response = f"""HTTP/1.1 200 OK
Content-Type: text/html
Connection: close

<!DOCTYPE html>
<html>
<head><title>Socket Server</title></head>
<body>
    <h1>Hello from a Socket!</h1>
    <p>This is raw HTTP over TCP.</p>
    <p>No Flask, no http.server - just sockets!</p>
    <p><strong>You are visitor #{request_count}</strong></p>
</body>
</html>
"""
    
    client_socket.send(http_response.encode())
    client_socket.close()
