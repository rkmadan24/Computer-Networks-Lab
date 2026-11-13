
from socket import *

serverName = "127.0.0.1"
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName, serverPort))

filename = input("Enter file name: ")

clientSocket.send(filename.encode())

filecontents = clientSocket.recv(4096).decode()

print("\nFrom Server:\n")
print(filecontents)

clientSocket.close()
