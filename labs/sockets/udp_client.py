import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = '127.0.0.1'
port = 9090

message = "Hello from UDP client!"
client_socket.sendto(message.encode(), (host, port))
print(f"Sent to {host}:{port}")

data, server_address = client_socket.recvfrom(1024)
print(f"Received from {server_address}: {data.decode()}")

client_socket.close()
