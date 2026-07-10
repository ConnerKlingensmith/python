import socket

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Create TCP socket
HOST = '127.0.0.1'
PORT = 8080

server_socket.bind((HOST, PORT))

# Listen for incoming connections (max 5 in queue)
server_socket.listen(5)
print(f"TCP Server listening on {HOST}:{PORT}")

# COnnection counter
connection_count = 0

# Keep server running
while True:
    # Accept a connection (blocks until client connects)
    client_socket, client_address = server_socket.accept()
    connection_count += 1
    print(f"COnnection #{connection_count} from {client_address}")

    # Receive data from client
    data = client_socket.recv(1024) # Buffer size 1024 bytes
    print(f"Received: {data.encode()}")

    # Send response with counter to client
    response = f"Hello! You are connection #{connection_count}"
    client_socket.send(response.encode())

    # Close this client connection (but keep server running)
    client_socket.close()
