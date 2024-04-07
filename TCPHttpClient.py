from socket import *
import time
import argparse

HOST = 'localhost'
PORT = 12000

reqLine = 'GET /index.html HTTP/1.1\r\n'
reqHost = 'Host: www-net.cs.umass.edu\r\n'
reqConn = 'Connection: keep-alive\r\n'
reqKeep = 'Keep-Alive: timeout=5,max=1000\r\n'
reqLen = 'Content-Length: 10101\r\n'
reqEnd = '\r\n'

# Header:
# Request line
# Header (fields)
# \n

req = reqLine + reqHost + reqConn + reqKeep + reqLen + reqEnd

def persistent():
	# SOCK_STREAM for TCP mode
    sock = socket(AF_INET, SOCK_STREAM)
    # Try to connect to the specified server
    sock.connect((HOST, PORT))
		
	# Never close connection till timeout
	# ... or it exceeds req limit
	# Response time: 2RTT + n * transmission time
		
    t1 = time.time()
    print(('Requesting #1'))
    sock.send(req.encode())
    sock.recv(1024)
    
    t2 = time.time()
    print('Requesting #2')
    sock.send(req.encode())
    sock.recv(1024)

    t3 = time.time()
    print('Requesting #3')
    sock.send(req.encode())
    sock.recv(1024)

    sock.close()
    t4 = time.time()

    print(f'Req #1: {t2 - t1}\nReq #2: {t3 - t2}\nReq #3: {t4 - t3}')

def nonPersistent():
    t1 = time.time()
	# SOCK_STREAM for TCP connection
    sock = socket(AF_INET, SOCK_STREAM)
    
    # Open / Close connection per every request
	# Response time: n * (2RTT + transmission time)
    
    # Try to connect to the specified server
    sock.connect((HOST, PORT))
    print(('Requesting #1'))
    sock.send(req.encode())
    sock.recv(1024)
    sock.close()
    
    t2 = time.time()
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((HOST, PORT))
    print('Requesting #2')
    sock.send(req.encode())
    sock.recv(1024)
    sock.close()

    t3 = time.time()
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((HOST, PORT))
    print('Requesting #3')
    sock.send(req.encode())
    sock.recv(1024)
    sock.close()

    t4 = time.time()

    print(f'Req #1: {t2 - t1}\nReq #2: {t3 - t2}\nReq #3: {t4 - t3}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', action='store_true')
    parser.add_argument('-np', action='store_true')
    args = parser.parse_args()
    if args.p:
        persistent()
    else:
        nonPersistent()