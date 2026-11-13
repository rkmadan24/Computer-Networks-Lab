
from socket import *

serverPort = 12000

# Create UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Bind socket to port 12000
serverSocket.bind(('', serverPort))

print("The server is ready to receive")

while True:
    # Receive filename from client
    message, clientAddress = serverSocket.recvfrom(2048)

    filename = message.decode()

    print("Requested file:", filename)

    try:
        # Open the requested file
        with open(filename, 'r') as file:
            fileContent = file.read()

        # Send file contents to client
        serverSocket.sendto(
            fileContent.encode(), clientAddress
        )

    except FileNotFoundError:
        # Send error if file does not exist
        errorMessage = "Error: File not found"
        serverSocket.sendto(
            errorMessage.encode(), clientAddress
        )
