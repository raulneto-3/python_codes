import socket
from queue import Queue
import threading

target = '127.0.0.1'

q = Queue()
for port in range(1, 1025):
    q.put(port)

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False
    
def worker():
    while not q.empty():
        port = q.get()
        if portscan(port):
            print('Port', port, 'is open!')
        else:
            print('Port', port, 'is closed.')

for t in range(100):
    thread = threading.Thread(target=worker)
    thread.start()
