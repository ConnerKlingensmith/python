import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = '127.0.0.1'
PORT = 8080

client_socket.connect((HOST, PORT))
print(f"Connected to {HOST}, {PORT}")

# Send message to server
message = "Hello from client!"
client_socket.send(message.encode())

# Receive response from server
data = client_socket.recv(1024)
print(f"Received: {data.decode()}")

# Close connection
client_socket.close()
