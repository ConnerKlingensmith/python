import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = '127.0.0.1'
port = 9090

server_socket.bind((host, port))
print(f"UDP Server listening on {host}:{port}")

message_count = 0

while True:
    data, client_address = server_socket.recvfrom(1024)
    message_count += 1
    print(f"\nMessage #{message_count} from {client_address}: {data.decode()}")

    response = f"Received! Message #{message_count}"
    server_socket.sendto(response.encode(), client_address)
