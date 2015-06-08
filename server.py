import socket
import sys
from thread import *

HOST = '127.0.0.1'
PORT = 8888
answer = "U fakken w00t m8"

# Socket Creation
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#First argument: type of network (in this case, IPv4), second argument: type of transfer protocol (in this case, TCP)
print 'Socket created'

#Socket Binding
try:
    s.bind((HOST, PORT)) #The argument of the binding is a tuple consisting in the host and the port...previously/arbitrary determined
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

print 'Socket bind complete'
s.listen(10) #Awaits for connections in the binded host and port
print 'Socket now listening'

def clientthread(conn,addr): # This is the thread for each client
    #conn.send('Welcome to the server!\n')
    while True: #infinite loop to keep the thread running
        try:
            it = int(conn.recv(1024))
        except socket.error:
            break;
        print "Now sending %d messages to %s / %d" %(it,addr[0],addr[1])
        while(it):
            conn.sendall(answer)
            it -= 1
    print "Connection ended with %s:%s" % addr
    conn.close()

while 1:
    #wait to accept a connection
    conn, addr = s.accept()
    #display client information
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    start_new_thread(clientthread,(conn,addr))

s.close()
