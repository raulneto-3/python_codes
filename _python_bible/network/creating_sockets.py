import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET is the address family for IPv4

# SOCK_STREAM is the socket type for TCP
# SOCK_DGRAM is the socket type for UDP

host = '127.0.0.1'
port = 9999
backlog = 5
bufsize = 1024
address = (host, port)  

# Socket Methods
s.bind((host, port)) # Bind the socket to an address
s.listen(backlog) # Enable a server to accept connections
s.accept() # Accept a connection. The return value is a pair (conn, address) where conn is a new socket object usable to send and receive data on the connection, and address is the address bound to the socket on the other end of the connection.

s.recv(bufsize) # Receive data from the socket. The return value is a bytes object representing the data received. The maximum amount of data to be received at once is specified by bufsize.
s.send(bytes) # Send data to the socket. The socket must be connected to a remote socket. Returns the number of bytes sent. Applications are responsible for checking that all data has been sent; if only some of the data was transmitted, the application needs to attempt delivery of the remaining data.
s.reevfrom(bufsize) # Receive data from the socket. The return value is a pair (bytes, address) where bytes is a bytes object representing the data received and address is the address of the socket sending the data.
s.sendto(bytes, address) # Send data to the socket. The socket should not be connected to a remote socket, since the destination socket is specified by address. Returns the number of bytes sent. Note that if the underlying network is UDP, the application may not be able to determine when all data has been successfully delivered to the destination.
s.close() # Close the socket. All future operations on the socket object will fail. The remote end will receive no more data (after queued data is flushed).
s.gethostname() # Return a string containing the hostname of the machine where the Python interpreter is currently executing.