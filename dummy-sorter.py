#! /usr/bin/env python3
import socket
import binascii
from protocol import read_protocol_packet

UDP_IP = "" #equivalent to IPADDR_ANY
UDP_PORT = 13337

sock = socket.socket(socket.AF_INET, #IP
	socket.SOCK_DGRAM) #UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
	try:
		source, datatype, payload = read_protocol_packet(sock)
		print("Received packet:")
		print("From:", source[0] + ":" + str(source[1]))
		print("Datatype:", binascii.hexlify(datatype))
		print("Payload:", binascii.hexlify(payload))
	except ConnectionError as e:
		print(e)
	