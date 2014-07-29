#! /usr/bin/env python3
import socket
from protocol import *
import sys
import queue, threading

def receive_packets(sock, type, q):
	while True:
		payload = sock.recv(2**16)
		#print(payload)
		q.put(create_protocol_packet(type, payload))

UDP_IP = "sorter.local"
PROTOCOL_TAG = 1
UDP_PORT = 13337
NUM_TAGS = 4

socks = list()
#print("0")
for i in range(NUM_TAGS):
	s = socket.socket(socket.AF_INET, #IP
		socket.SOCK_DGRAM)
	s.bind(("", UDP_PORT + i))
	socks.append(s)
	#print(s)

"""listen_sock = socket.socket(socket.AF_INET, #IP
	socket.SOCK_DGRAM) #UDP
listen_sock.bind(("", UDP_PORT))"""
#print("1")
send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
send_sock.connect((UDP_IP, UDP_PORT))
#print("2")

#log = open("forwarder_log", "wb")
q = queue.Queue()
for index, sock in enumerate(socks):
	#print (str(sock))
	t = threading.Thread(target = receive_packets, args = (sock, index + 1, q))
	t.daemon = True
	t.start()
#print("3")
while True:
	"""payload = listen_sock.recv(2**16)
	print("Received packet size", len(payload))
	log.write(payload)
	log.flush()
	packet = create_protocol_packet(PROTOCOL_TAG, payload)"""
	try:
		#print("waiting")
		packet = q.get(True, 2)
		print("Received packet size", len(packet) - 6)
		send_sock.sendall(packet)
	except queue.Empty:
		pass