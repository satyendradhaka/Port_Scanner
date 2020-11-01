#!/bin/python3

import time
import sys
import socket
from datetime import datetime

#Define target
if len(sys.argv) == 4 and sys.argv[3].isdigit() and sys.argv[2].isdigit():
	target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPv4
else:
	print("====================================================")
	print("Invalid input detected")
	print("Syntax: python3 port_scanner.py 10.10.0.3 1 80")
	print("======  python3 port_scanner.py <ip> <min port> <maxport>")
	print("====================================================")
	sys.exit()
#Banner
print("-" * 50)
print("Scanning target "+target)
print("Time started: "+str(datetime.now()))
print("-" * 50)


openpts = []
minpt = int(sys.argv[2])
maxpt = int(sys.argv[3])

def nl():
	print("\n")


try:
	for port in range(minpt,maxpt+1):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port)) #returns error
		print("Checking port {}. . .".format(port))
		if result == 0:
			print("Port {} is open".format(port))
			openpts.append("{}".format(port))
		s.close()


#error handling

except KeyboardInterrupt:
    print('exiting program')
    sys.exit()
except socket.gaierror:
    print("couldn't resolve hostname")
    sys.exit()
except socket.error:
    print("could not connect to host")
    sys.exit()

#display final results.

print("There are "+str(len(openpts))+" ports open.")
print("Concluded: "+str(datetime.now()))
print("+","-" * 16,"+")
if not openpts:
	print("No open ports!")
	sys.exit()
else:
	for p in openpts: 
		print("| Port {} is open! |".format(p))
		print("+------------------+")
