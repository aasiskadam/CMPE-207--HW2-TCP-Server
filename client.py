import socket			 
import time 

# Create a socket object 
s = socket.socket()		 

# Define the port on which you want to connect 
port = 50005				

# connect to the server on local computer 
s.connect(('10.0.0.154', port)) 

time.sleep(3)
# receive data from the server 
print (s.recv(2048)) 

# close the connection 
s.close()
