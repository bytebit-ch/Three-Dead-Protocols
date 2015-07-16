
import socket
HOST = 'localhost'
PORT = 5555   #our port from before
ADDR = (HOST,PORT)
BUFSIZE = 1024

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((ADDR))

quote_sent = client.recv(BUFSIZE)


quote_sent = quote_sent.decode('utf-8') #client decoding 
print(quote_sent)

client.close()