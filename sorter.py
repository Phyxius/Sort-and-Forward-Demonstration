import socket
from protocol import *
from util import *

FORWARD_TABLE = { b"0001":"192.168.1.1", b"0002":"192.168.1.2", b"0003":"192.168.1.3", b"0004":"192.168.1.4" }

UDP_IP = "" #equivalent to IPADDR_ANY
UDP_PORT = 13337

sock = socket.socket(socket.AF_INET, #IP
	socket.SOCK_DGRAM) #UDP
sock.bind((UDP_IP, UDP_PORT))

client_sock = socket.socket(socket.AF_INET, #IP
	socket.SOCK_DGRAM) #UDP

while True:
	try:
		source, datatype, payload = read_protocol_packet(sock)
		print("Received packet from {} with datatype {} and payload length {}".format(
			source[0] + ":" + str(source[1]), datatype, len(payload)))
		destination = FORWARD_TABLE[datatype] if datatype in FORWARD_TABLE else FORWARD_TABLE[b"0004"]
		print("\tForwarded to", destination)
		client_sock.sendto(payload, (destination, UDP_PORT))
	except ConnectionError as e:
		print(e)