#!/usr/bin/env python3
import socket
import sys

IDENTIFIERS = { 
	"0x11" : "10.0.2.21", #audio
	"0x22" : "10.0.3.21", #video
	"0x33" : "10.0.4.21", #text
	"0x44" : "10.0.5.21"  #auxiliary
}


sock = socket.socket(socket.AF_INET, #IP
	socket.SOCK_DGRAM) #UDP
LISTEN_IP = "" #aka IPADDR_ANY
if len(sys.argv) > 1:
	if sys.argv[1] in IDENTIFIERS:
		LISTEN_IP = IDENTIFIERS[sys.argv[1]]
	else:
		LISTEN_IP = sys.argv[1]

sock.bind((LISTEN_IP, 13337))

out = sys.stdout

while True:
	out.buffer.write(sock.recvfrom(4096)[0])
	out.flush()