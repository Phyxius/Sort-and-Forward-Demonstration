#! /usr/bin/env python3
import socket
from protocol import *
from util import *

FORWARD_TABLE = { 
	0x11 : "10.0.2.21", #audio
	0x22 : "10.0.3.21", #video
	0x33 : "10.0.4.21", #text
	0x44 : "10.0.5.21"  #auxiliary
}

UDP_IP = "" #equivalent to IPADDR_ANY
UDP_PORT = 13337

server_sock = socket.socket(socket.AF_INET, #IP
	socket.SOCK_DGRAM) #UDP
server_sock.bind((UDP_IP, UDP_PORT))

log = open("sorter_log", "wb")

SOCK_TABLE = dict()
for key in FORWARD_TABLE: #create sockets for each forward destination
	value = FORWARD_TABLE[key]
	sock = socket.socket(socket.AF_INET, #IP
		socket.SOCK_DGRAM) #UDP
	sock.connect((value, UDP_PORT))
	SOCK_TABLE[key] = sock

while True:
	try:
		source, datatype, payload = read_protocol_packet(server_sock)
		print("Received packet from {} with datatype {} and payload length {}".format(
			source[0] + ":" + str(source[1]), datatype, len(payload)))
		destination = SOCK_TABLE[datatype] if datatype in FORWARD_TABLE else FORWARD_TABLE[0x44]
		print("\tForwarded to", FORWARD_TABLE[datatype] if datatype in FORWARD_TABLE else FORWARD_TABLE[0x44])
		log.write(payload)
		log.flush()
		destination.sendall(payload)
	except ConnectionError as e:
		print(e)