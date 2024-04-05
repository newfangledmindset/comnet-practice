from socket import *
from RequestValidator import *
import time
import argparse

def parseHeader(conn: socket):
    rawReq = conn.recv(1024)
    req = rawReq.decode()
    if not req:
        return
    method = req.split()[0]
    if not isReqMsg(req) or not isReqLine(req):
        conn.send('HTTP/0.1 400 Bad Request'.encode())
    elif method != 'GET' and method != 'POST':
        print(method)
        conn.send('HTTP/0.1 405 Method Not Allowed'.encode())
    else:
        print(f"Req size: {len(req)}\n{req}")
        if method == 'GET' and isReqMsg(req):
            conn.send('HTTP/0.1 200 OK'.encode())

        if method == 'POST':
            if not isLengthExists(req):
                conn.send('HTTP/0.1 411 Length Required'.encode())
            else:
                conn.send('HTTP/0.1 404 Not Found'.encode())

def persistentConn(sock: socket, timeout: int):
    t1 = time.time()
    conn, addr = sock.accept()
    print('Connection established.')

    while True:
        if (time.time() - t1 > timeout):
            break
        parseHeader(conn)    
    conn.close()
    print('Connection Lost.')

def nonPersistentConn(sock: socket):
    while True:
        conn, addr = sock.accept()
        print('Connection established.')
        parseHeader(conn)
        conn.close()
        print('Connection lost.\n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', action='store_true')
    parser.add_argument('-np', action='store_true')
    args = parser.parse_args()
    PORT = 12000
    SOCKET = socket(AF_INET, SOCK_STREAM)
    SOCKET.bind(('', PORT))
    SOCKET.listen(1)
    print("The server is ready to receive")
    while True:
        try:
            if args.p:
                persistentConn(SOCKET, 5)
            else:
                nonPersistentConn(SOCKET)
        except KeyboardInterrupt:
            SOCKET.close()
            break
