#-------------------------------------TCPCLIENT------------------------#
                #-----------------------------------------------#
#----------------------------------------------------------------------#
import socket   
import sys

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = raw_input("What is the host:") #enter the ip or website
port = input("What is port:") #enter the port of connection

client.connect((host,port)) #connection starting
client.send("GET / HTTP/1.1\r\nHOST: \r\n\r\n") #sending random data
response = client.recv(4096) #receving the response from  server
print response #now print the response
