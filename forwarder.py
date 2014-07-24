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

log = open("forwarder_log", "wb")

while True:
	payload = listen_sock.recv(2**16)
	print("Received packet size", len(payload))
	log.write(payload)
	log.flush()
	packet = create_protocol_packet(1, payload)
	send_sock.sendall(packet)