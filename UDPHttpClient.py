from socket import *
HOST = 'localhost'
PORT = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

reqLine = 'POST /index.html HTTP/1.1\r\n'
reqHost = 'Host: www-net.cs.umass.edu\r\n'
reqConn = 'Connection: keep-alive\r\n'
reqLen = 'Content-Length: 10101\r\n'
reqEnd = '\r\n'

req = reqLine + reqHost + reqConn + reqLen + reqEnd

clientSocket.sendto(req.encode(), (HOST, PORT))
res, addr = clientSocket.recvfrom(2048)
print(f"size: {len(res)}\n{res.decode()}")
clientSocket.close()