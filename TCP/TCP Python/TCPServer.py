import socket
import sys
 
HOST = '127.0.0.1'
PORT = 5005
BUFFER_SIZE = 20
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket created')
s.bind((HOST, PORT))	 
print ('Socket bind complete')
s.listen(10)
print ('Socket now listening')
 
while 1:
	conn, addr = s.accept()
	print ('Connected with {} : {}'.format(addr[0], str(addr[1])))
	data = conn.recv(BUFFER_SIZE)
	print ("received data: {}".format( data ))
	data = data.upper()
	conn.send(data)
	 
s.close()