import socket

client = socket.socket()

client.connect(("localhost", 9040))

print("Connected to the server")

while True:
    message = input("Client: ")

    client.send(message.encode())

    if message == "exit":
        break

    reply = client.recv(1024).decode()

    if reply == "exit":
        print("Server disconnected.")
        break

    print("Server:", reply)

client.close()
