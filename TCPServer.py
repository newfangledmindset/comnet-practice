from socket import *
PORT = 12000
SOCKET = socket(AF_INET, SOCK_STREAM)
SOCKET.bind(('', PORT))
SOCKET.listen(1)
print("I'm ready")
while True:
    conn, addr = SOCKET.accept()
    msg = conn.recv(1024)
    modMsg = msg.decode().upper()
    conn.send(modMsg.encode())
    conn.close()