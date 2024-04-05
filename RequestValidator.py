def isReqLine(req: str) -> bool:
    reqLine = req.split('\r\n')[0]
    method = reqLine.split()[0]
    if (method != 'GET' and method != 'POST' and method != 'PUT' and method != 'DELETE') or len(reqLine.split(' ')) != 3:
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