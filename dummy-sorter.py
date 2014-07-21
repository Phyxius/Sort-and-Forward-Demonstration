#! /usr/bin/env python3
import socket
import binascii
from protocol import *

UDP_IP = "" #equivalent to IPADDR_ANY
UDP_PORT = 13337

sock = socket.socket(socket.AF_INET, #IP
	socket.SOCK_DGRAM) #UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
	try:
		source, datatype, payload = read_protocol_packet(sock)
		datatype = binascii.hexlify(bytes([ datatype ])).zfill(4)
		if datatype in PROTOCOL_DATA_TYPES:
			datatype = PROTOCOL_DATA_TYPES[datatype]
		if datatype == "Text":
			payload = payload.decode("utf-8")
		else:
			payload = binascii.hexlify(payload)
		print("Received packet from", source[0] + ":" + str(source[1]))
		print("Datatype:", datatype)
		print("Payload:", payload)
	except ConnectionError as e:
		print(e)