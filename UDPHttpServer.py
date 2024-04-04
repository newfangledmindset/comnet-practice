from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready to receive")

def isReqLine(req: str) -> bool:
    reqLine = req.split('\r\n')[0]
    method = reqLine.split()[0]
    if (method != 'GET' and method != 'POST' and method != 'PUT' and method != 'DELETE') or len(reqLine.split(' ')) != 3:
        print(f"{reqLine.split()[0]}, {reqLine.split()[0] != 'POST'}, {len(reqLine.split(' '))}\n")
        return False
    
    return True

def isReqMsg(req: str) -> bool: 
    headerLines = req.splitlines()[1:-1]
    if req[-4:] != '\r\n\r\n':
        return False
    
    for header in headerLines:
        substr = header.split()
        if (len(substr) != 2 or substr[0][-1] != ':'):
            return False
        
    return True

def isLengthExists(req: str) -> bool:
    headerLines = req.splitlines()[1:-1]
    for header in headerLines:
        field = header.split()[0]
        if (field == "Content-Length:"):
            return True
    
    return False

while True:
    rawReq, clientAddress = serverSocket.recvfrom(2048)
    req = rawReq.decode()
    method = req.split()[0]
    if not isReqMsg(req) or not isReqLine(req):
        serverSocket.sendto('HTTP/0.1 400 Bad Request'.encode(), clientAddress)
    elif method != 'GET' and method != 'POST':
        print(method)
        serverSocket.sendto('HTTP/0.1 405 Method Not Allowed'.encode(), clientAddress)
    else:
        print(f"Req size: {len(req)}\n{req}")
        if method == 'GET' and isReqMsg(req):
            print(f"Req size: {len(req)}")
            serverSocket.sendto('HTTP/0.1 200 OK'.encode(), clientAddress)

        if method == 'POST':
            if not isLengthExists(req):
                serverSocket.sendto('HTTP/0.1 411 Length Required'.encode(), clientAddress)
            else:
                serverSocket.sendto('HTTP/0.1 404 Not Found'.encode(), clientAddress)
