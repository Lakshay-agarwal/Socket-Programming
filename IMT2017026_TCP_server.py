# Importing socket library
import socket

def Sort_Ascending(s):
  res = []
  res_str = ''
  for i in s.split():
    res.append(int(i))
  res.sort()
  for i in res:
    res_str += str(i) + ' '
  return res_str

IP = ''
port = 5000
buffer_size = 20

# Creating a socket object
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Bind to a specific IP and port
s.bind((IP,port))

# Socket put in listening mode
s.listen(1)

con,addr = s.accept()
print "Established connection with " , addr

while True:
  data = con.recv(buffer_size)
  ans = Sort_Ascending(data)
  if not data: break
  print "Numbers sorted in ascending order - " ,ans
  con.send(ans)
con.close()
print "Connection closed"
