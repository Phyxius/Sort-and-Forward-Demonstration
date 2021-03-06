#! /usr/bin/env python3
import socket
import binascii
import sys

UDP_IP = sys.argv[1] if len(sys.argv) > 1 else "" #equivalent to IPADDR_ANY
UDP_PORT = 13337

sock = socket.socket(socket.AF_INET, #IP
	socket.SOCK_DGRAM) #UDP
sock.bind((UDP_IP, UDP_PORT))

print("Listening on {}:{}...".format(UDP_IP, UDP_PORT))

while True:
	data, addr = sock.recvfrom(1024)
	print("Received Message from {}:".format(addr), data)
