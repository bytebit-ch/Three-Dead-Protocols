
import socket
HOST = 'localhost'
PORT = 13   #our port from before
ADDR = (HOST,PORT)
BUFSIZE = 1024

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((ADDR))

data = client.recv(BUFSIZE)


data = data.decode('utf-8') #client decoding 
print(data)

client.close()