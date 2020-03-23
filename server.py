import socket
#creating a socket object 
s = socket.socket()		 
print ("Successfully created socket, now waiting for connections form clients:  ") 
# Chosing a port number 12345
port = 50005				
# Bind to the port 
s.bind(('', port))		 
print ("socket binded to %s" %(port)) 
# call listening from   
s.listen(5)	 
print ("socket is listening for connectoins")			
#create a loop to accept multiple connectoin
while True: 
    # Establish connection with client. 
    c, addr = s.accept()	 
    print ('Got connection from', addr)
    ##############- Send the message1
    msg =" Hello, world!  "
    b1 = bytes(msg, encoding = 'utf-8')
    # send massege to client 
    c.send(b1)
    ############### send message 2
    msg2 ="  ---------   "
    b2 = bytes(msg2, encoding = 'utf-8')
    # send massege to client 
    c.send(b2)
    ############## send message 3
    msg3="  Sending multiple messages  "
    b3 = bytes(msg3, encoding = 'utf-8')
    # send massege to client 
    c.send(b3)
    ############### send message 4
    msg4 =" ^^^^^^^^^^^^^ "
    b4 = bytes(msg4, encoding = 'utf-8')
    # send massege to client 
    c.send(b4)
    ############## send message 5
    msg5 ="   BaBye    "
    b5 = bytes(msg5, encoding = 'utf-8')
    # send massege to client 
    c.send(b5)
    # Close the connection with the client 
    c.close() 
