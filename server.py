import socket
import sys
from threading import Thread
from thread import *

if (len(sys.argv) != 4):
    print("Please enter the following parameters in order:\n The ip adress, the port and the type of the Transfer Protocol (TCP or UDP)")
    sys.exit()
HOST = sys.argv[1]
PORT = int(sys.argv[2])
answer = "a"
lol = 50
for i in range(0,lol-1):
    answer += 'a'

# Socket Creation
if(sys.argv[3] == "TCP"):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
else:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#First argument: type of network (in this case, IPv4), second argument: type of transfer protocol (in this case, TCP)
print 'Socket created'

#Socket Binding
try:
    s.bind((HOST, PORT)) #The argument of the binding is a tuple consisting in the host and the port...previously/arbitrary determined
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

print 'Socket bind complete'
if (sys.argv[3] == "TCP"):
    s.listen(10) #Awaits for connections in the binded host and port
    print 'Socket now listening on %s / %d' % (HOST,PORT)

def clientthread(conn,addr): # This is the thread for each client
    try:
        it = int(conn.recv(8))
    except socket.error:
        conn.close();
    except ValueError:
        conn.close();
    print "Now sending %d messages to %s / %d" %(it,addr[0],addr[1])
    while(it):
        try:
            conn.sendall(answer)
        except socket.error:
            break;
   	it -= 1
    conn.close()
    #print "Connection ended with %s:%s" % addr

def clientUDP(msg,addr):
    print("Now sending %d messages to %s / %d") %(msg,addr[0],addr[1])
    while(msg > 0):
	msg -= 1
	s.sendto(answer, addr)

if(sys.argv[3] == "UDP"):
	print("The server is on at the adress: %s / %d") %(HOST,PORT)

if (sys.argv[3] == "TCP"):
	while 1:
		    #wait to accept a connection
		    conn, addr = s.accept()
		    #print 'Connected with ' + addr[0] + ':' + str(addr[1])
		    start_new_thread(clientthread,(conn,addr))
else:
    while 1:
	    msg, addr = s.recvfrom(1024)
	    msg = int(msg)
	    t = Thread(target=clientUDP,args=(msg,addr))
	    t.start() 
s.close()
