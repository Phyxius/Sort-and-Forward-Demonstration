#! /usr/bin/env python3
import socket
import protocol

UDP_IP = "" #equivalent to IPADDR_ANY
UDP_PORT = 13337

sock = socket.socket(socket.AF_INET, #IP
	socket.SOCK_DGRAM) #UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
	print(read_protocol_packet(sock))
	