# Import socket library
import socket

#IPv4 Address of server over IIITB-Zone-BM
IP = '172.16.85.157'

port = 5000
buffer_size = 1024
message = raw_input("Enter 5 numbers with spaces \n")

# Creating a socket object
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Connect to the server
s.connect((IP,port))

s.send(message)
data = s.recv(buffer_size)

# Connection closed
s.close()

print "Numbers sorted in ascending order"
print data
