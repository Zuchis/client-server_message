import socket   #for sockets
import sys  #for exit
import time

try: #Socket Creation
    #create an AF_INET(IPv4), STREAM socket (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit();

print 'Socket Created'
host = "127.0.0.1"
port = 8888
msg = 1000
times = []
request = "rck"
f = open("output.txt","w")
#connect to the server
s.connect((host , port))
print 'Socket Connected to ' + host + ' on port ' + str(port)

while(msg != 3500):
    msgSent = str(msg)
    try :
        s.sendall(msgSent) # Send the number of messages to be received
    except socket.error:
        #Send failed
        print 'Send failed'
        break;

    print "Now Receiving %d messages from Server:" % msg
    for it in range(0,msg):
        current = it+1
        total = 0
        try:
            start = time.time()
            reply = s.recv(10)
            end = time.time()
            t = end-start
            total += t
            print "Message %d received" % current
            print t
        except socket.error:
            print "Message %d not received" % current
        print
    total /= msg
    times.append(total)
    avrg = str(msg) + "    " + str(total) + "\n"
    f.write(avrg)
    msg += 500
print (times)
s.close()
