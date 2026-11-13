
from socket import *

serverName = 'localhost'
serverPort = 12000

# Create UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Get filename from user
filename = input("Enter the filename: ")

# Send filename to server
clientSocket.sendto(
    filename.encode(), (serverName, serverPort)
)

# Receive file contents from server
fileContent, serverAddress = clientSocket.recvfrom(65535)

# Display received contents
print("\nFile contents:")
print(fileContent.decode())

# Close socket
clientSocket.close()
