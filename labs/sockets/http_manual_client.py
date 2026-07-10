import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 80

client_socket.connect((host, port))
print(f"Connected to {host}:{port}")

http_request = "GET / HTTP/1.1\r\nHost: localhost\r\nConnection: close\r\n\r\n"
client_socket.send(http_request.encode())
print(f"Send HTTP request")
print(http_request)

response = b""
while True:
    chunk = client_socket.recv(4096)
    if not chunk:
        break
    response += chunk

client_socket.close()

print("\nReceived HTTP response:")
print(response.decode())
