from socket import *
from RequestValidator import *

PORT = 12000
SOCKET = socket(AF_INET, SOCK_DGRAM)
SOCKET.bind(('', PORT))
print("The server is ready to receive")

while True:
    rawReq, clientAddress = SOCKET.recvfrom(2048)
    req = rawReq.decode()
    method = req.split()[0]
    if not isReqMsg(req) or not isReqLine(req):
        SOCKET.sendto('HTTP/0.1 400 Bad Request'.encode(), clientAddress)
    elif method != 'GET' and method != 'POST':
        print(method)
        SOCKET.sendto('HTTP/0.1 405 Method Not Allowed'.encode(), clientAddress)
    else:
        print(f"Req size: {len(req)}\n{req}")
        if method == 'GET' and isReqMsg(req):
            print(f"Req size: {len(req)}")
            SOCKET.sendto('HTTP/0.1 200 OK'.encode(), clientAddress)

        if method == 'POST':
            if not isLengthExists(req):
                SOCKET.sendto('HTTP/0.1 411 Length Required'.encode(), clientAddress)
            else:
                SOCKET.sendto('HTTP/0.1 404 Not Found'.encode(), clientAddress)
