import socket

target = '127.0.0.1'

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False
    
for portNumber in range(1, 1025):
    if portscan(portNumber):
        print('Port', portNumber, 'is open!')
    else:
        print('Port', portNumber, 'is closed.')