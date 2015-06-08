import socket   #for sockets
import sys  #for exit
import time

#try: #Socket Creation
    #create an AF_INET(IPv4), STREAM socket (TCP)
    #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#except socket.error, msg:
#    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
#    sys.exit();

#print 'Socket Created'
host = "127.0.0.1"
port = 8888
msg = 1000
lol = 10485760
times = []
f = open("output.txt","w")
#connect to the server
#s.connect((host , port))
#print 'Socket Connected to ' + host + ' on port ' + str(port)

while(msg != 10100):
    msgSent = str(msg)
    try :
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host , port))
        print 'Socket Connected to ' + host + ' on port ' + str(port)
        s.send(msgSent) # Send the number of messages to be received
    except socket.error:
        #Send failed
        print 'Send failed'
        break;

    print "Now Receiving %d messages from Server:" % msg
    start = time.time()
    for it in range(0,msg):
        try:
            reply = s.recv(lol)
        except socket.error:
            print "Message %d not received" % (it)
    end = time.time()
    t = end-start
    print("Finished receiving %d messages in %lf seconds\n") %(msg,t)
    times.append(t)
    avrg = str(msg) + "    " + str(t) + "\n"
    f.write(avrg)
    msg += 100
print (times)
s.close()
