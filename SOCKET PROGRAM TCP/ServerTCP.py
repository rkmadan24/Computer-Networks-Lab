
from socket import *

serverName = "127.0.0.1"
serverPort = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind((serverName, serverPort))

serverSocket.listen(1)

while True:
    print("The server is ready to receive")

    connectionSocket, addr = serverSocket.accept()

    filename = connectionSocket.recv(1024).decode()

    try:
        file = open(filename, "r")
        contents = file.read()
        file.close()

        connectionSocket.send(contents.encode())

        print("Sent contents of", filename)

    except FileNotFoundError:
        connectionSocket.send("File not found".encode())

    connectionSocket.close()
