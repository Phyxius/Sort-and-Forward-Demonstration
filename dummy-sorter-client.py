#!/usr/bin/env python3
import socket
import binascii
from protocol import *

UDP_IP = "192.168.245.129"
UDP_PORT = 13337

sock = socket.socket(socket.AF_INET, #IP
	socket.SOCK_DGRAM) #UDP

while True:
	packet = create_protocol_packet(int(default_input("Datatype", "0x0001"), 16),
		default_input("Payload", "Test"), 
		int(default_input("Protocol Header", "0x09F9"), 16))
	sock.sendto(packet, (UDP_IP, UDP_PORT))
	print("Sent packet:", binascii.hexlify(packet))