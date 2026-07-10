import socket

server1 = socket.socket()
server1.bind(("localhost",9040))

server1.listen()
print("waiting")

client_socket,address = server1.accept()
print("client connected")

print(address)
