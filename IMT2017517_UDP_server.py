# Import socket library
import socket

def Sort_Descending(s):
  res = []
  res_str = ''
  for i in s.split():
    res.append(int(i))
  res.sort(reverse = 1)
  for i in res:
    res_str += str(i) + ' '
  return res_str

IP_Address = ''
Port_No = 6000
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((IP_Address, Port_No))

while True:
		# Buffer size is 1024
    data, addr = s.recvfrom(1024) 
    ans = Sort_Descending(data) 
    s.sendto(ans,addr)
    print "Numbers sorted in descending order - " ,ans

s.close()
