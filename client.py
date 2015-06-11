import socket   #for sockets
import sys  #for exit
import time

if (len(sys.argv) != 5):
    print("Please enter the following parameters in order:\n The ip adress, the port, the maximum number of messages, and the type of the Transfer Protocol (TCP or UDP)")
    sys.exit()
HOST = sys.argv[1]
PORT = int(sys.argv[2])
msg = 1000
msgMax = int(sys.argv[3]) + 100
msg_size = 10
times = []
f = open("output.txt","w")

if (sys.argv[4] == "TCP"):
	while(msg != msgMax):
	    msgSent = str(msg)
	    try :
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((HOST , PORT))
		print 'Socket Connected to ' + HOST + ' on port ' + str(PORT)
		s.send(msgSent) # Send the number of messages to be received
	    except socket.error:
		#Send failed
		print 'Send failed'
		break;

	    print "Now Receiving %d messages from Server:" % msg
	    start = time.time()
	    for it in range(0,msg):
		try:
		    reply = s.recv(msg_size)
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
else:
	while (msg != msgMax):
	    it = msg
	    n_bytes = msg_size * msg
	    msgSent = str(msg)
	    try :
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.sendto(msgSent,(HOST,PORT)) # Send the number of messages to be received
	    except socket.error:
		#Send failed
		print ('Send failed')
		break;

	    print ("Now Receiving %d messages from Server:") % (msg)
	    start = time.time()
	    #while(it > 0):
		#it -= 1
	    try:
	        d = s.recvfrom(n_bytes)
	    except socket.error:
	        print "Message %d not received" % (it)
	    end = time.time()
	    t = end-start
	    print("Finished receiving %d messages in %lf seconds\n") %(msg,t)
	    times.append(t)
	    avrg = str(msg) + "    " + str(t) + "\n"
	    f.write(avrg)
	    msg += 100
	    s.close()
	print (times)
