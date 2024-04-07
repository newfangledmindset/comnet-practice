from socket import *
HOST = 'localhost'
PORT = 12000

# SOCK_DGRAM for UDP mode

clientSocket = socket(AF_INET, SOCK_DGRAM)

reqLine = 'POST /index.html HTTP/1.1\r\n'
reqHost = 'Host: www-net.cs.umass.edu\r\n'
reqConn = 'Connection: keep-alive\r\n'
reqLen = 'Content-Length: 10101\r\n'
reqEnd = '\r\n'

req = reqLine + reqHost + reqConn + reqLen + reqEnd

# There's no 'connection' in UDP, so you have to mention (HOST, PORT) per every req send.

clientSocket.sendto(req.encode(), (HOST, PORT))

# Since we (client & server...) doesn't have connection, you have to specify what server to receive from.

res, addr = clientSocket.recvfrom(2048)
print(f"size: {len(res)}\n{res.decode()}")
clientSocket.close()