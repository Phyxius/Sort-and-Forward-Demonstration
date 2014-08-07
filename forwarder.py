#! /usr/bin/env python3
import socket
from protocol import *
import sys
import queue, threading
FORWARD_TABLE = {
	13337 : 0x11, #audio
	13338 : 0x22, #video
	13339 : 0x33, #text
	13340 : 0x44  #auxiliary
}
def receive_packets(sock, type, q): #receive packets, encapsulate them, and queue them for retransmission
	while True:
		payload = sock.recv(2**16)
		q.put(create_protocol_packet(type, payload))

UDP_IP = "sorter.local" #use local dns to resolve
PROTOCOL_TAG = 1
UDP_PORT = 13337
NUM_TAGS = 4

socks = list()
for i in range(NUM_TAGS): #create one socket per tag, on sequential ports starting at 13337
	s = socket.socket(socket.AF_INET, #IP
		socket.SOCK_DGRAM) #UDP
	s.bind(("", UDP_PORT + i))
	socks.append(s)
send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #IP/UDP
send_sock.connect((UDP_IP, UDP_PORT))

q = queue.Queue()
#tags = [ 0x11, 0x22, 0x33, 0x44 ]
#tags.reverse() #need to reverse for some reason. Idc why, really
for index, sock in enumerate(socks): #create a receiving thread for each socket
	t = threading.Thread(target = receive_packets, args = (sock, 0x11 * (index + 1), q))
	t.daemon = True
	t.start()
while True:
	try:
		packet = q.get(True, 2) #block for 2 secs or until there is something to dequeue
		print("Received packet size", len(packet) - 6)
		send_sock.sendall(packet)
	except queue.Empty:
		pass