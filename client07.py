
import socket
HOST = 'localhost'
PORT = 5555 #our port from before
ADDR = (HOST,PORT)
BUFSIZE = 1024

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((ADDR))

data = ''

while data != 'q':
	data = input("")
	data1 = data #used to update 'data' out of while loop because it is going to get encoded to send
	data = data.encode('utf-8')
	data = client.send(data)
	echoed_text = client.recv(BUFSIZE)
	echoed_text = echoed_text.decode('utf-8') 
	print(echoed_text)
	data = data1

client.close()

