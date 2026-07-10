import socket

client = socket.socket()

client.connect(("localhost",9040))

print("connected")
