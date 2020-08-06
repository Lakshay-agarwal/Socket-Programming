# Import socket library
import socket

#IPv4 Address of server over IIITB-Zone-BM
IP_Address = '172.16.86.9'

Port_No = 6000
message = raw_input("Enter 5 numbers with spaces \n")

# Creating a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(message, (IP_Address, Port_No))

data = s.recv(1024)

s.close()

print "Numbers sorted in descending order"
print data


