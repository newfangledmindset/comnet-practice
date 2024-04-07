from socket import *
serverName = 'localhost'
serverPort = 12000

# SOCK_DGRAM for UDP mode

clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input lowercase sentence:')

# There's no 'connection' in UDP, so you have to mention (HOST, PORT) per every req send.

clientSocket.sendto(message.encode(), (serverName, serverPort))
modifiedessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedessage.decode())
clientSocket.close()