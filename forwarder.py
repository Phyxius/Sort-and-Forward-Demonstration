#! /usr/bin/env python3
import socket
from protocol import *

UDP_IP = "sorter.local"
UDP_PORT = 13337

listen_sock = socket.socket(socket.AF_INET, #IP
	socket.SOCK_DGRAM) #UDP
listen_sock.bind(("", 13337))
send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
send_sock.connect((UDP_IP, UDP_PORT))


while True:
	packet = create_protocol_packet(1, listen_sock.recvfrom(2**16)[0])
	send_sock.sendall(packet)