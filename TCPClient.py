from socket import *
NAME = 'localhost'
PORT = 12000
SOCKET = socket(AF_INET, SOCK_STREAM)
SOCKET.connect((NAME, PORT))
msg = input("Input lowercase sentence:")
SOCKET.send(msg.encode())
modMsg = SOCKET.recv(1024)
print(f"Recieved from server: {modMsg.decode()}")
SOCKET.close()