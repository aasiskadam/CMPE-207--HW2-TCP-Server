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
    msg3="  The next is a picture of a dog: "
    b3 = bytes(msg3, encoding = 'utf-8')
    # send massege to client 
    c.send(b3)
    ############### send message 4
    msg4 ="O_______/"
    b4 = bytes(msg4, encoding = 'utf-8')
    # send massege to client 
    c.send(b4)
    msg5 ='                                                                                                               '
    b5 = bytes(msg5, encoding = 'utf-8')
    # send massege to client 
    c.send(b5)
	############## send message 6
    msg6 =" | | | |"
    b6 = bytes(msg6, encoding = 'utf-8')
    # send massege to client 
    c.send(b6)
	############## send message 7
    msg7 ="    Okay......Bye!!!"
    b7 = bytes(msg7, encoding = 'utf-8')
    # send massege to client 
    c.send(b7)
    # Close the connection with the client 
    c.close() 
