import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.11', 9999))
s.listen()
print('Server listening on port 9999')
while True:
    client, address = s.accept()
    print(f'Connection from {address} has been established!')
    client.send('Welcome to the server!'.encode(ascii))
    client.close()