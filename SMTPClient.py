# You can setup your own SMTP server!
# Check out https://github.com/rnwood/smtp4dev

from socket import *
HOST = 'localhost'
PORT = 25

msgArr = ["HELO asdf.net",
          "MAIL FROM: <alice@asdf.net>",
          "RCPT TO: <trudy@asdf.net>",
          "DATA",
          "Hello!",
          ".",
          "QUIT"]

SOCKET = socket(AF_INET, SOCK_STREAM)
SOCKET.connect((HOST, PORT))

for msg in msgArr:
    SOCKET.send(f"{msg}\r\n".encode())
    rMsg = SOCKET.recv(1024)
    print(rMsg.decode())

SOCKET.close()