
import socket  
import random

##let's set up some constants
HOST = ''    #we are the host
PORT = 5555   #sudo to use connect to port 13
ADDR = (HOST,PORT)    #we need a tuple for the address
BUFSIZE = 1024    #reasonably sized buffer for data

## now we create a new socket object (serv)
## see the python docs for more information on the socket types/flags

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
 
##bind our socket to the address
serv.bind((ADDR))    #the double parens are to create a tuple with one element
serv.listen(5)    #5 is the maximum number of queued connections we'll allow
print('listening...')

conn,addr = serv.accept() #accept the connection


quote = [["First quote - Me"], ["Second again - Me"], ["Third Test - Me"]]

quote_picker = random.choice(quote)



"""
bytes->string you decode
string->bytes you encode
the network requires bytes so to send a string, you need to encode it, 
send it on the network, then the client decodes it
"""
quote_send = str(quote_picker).encode('utf-8')


conn.send(quote_send)

conn.close()