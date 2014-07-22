import socket
from protocol import *
from util import *

FORWARD_TABLE = { 1:"192.168.245.130", 2:"192.168.245.131", 3:"192.168.245.132", 4:"192.168.245.133" }

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
			source[0] + ":" + str(source[1]), PROTOCOL_DATA_TYPES[datatype] if datatype in PROTOCOL_DATA_TYPES else datatype, len(payload)))
		destination = FORWARD_TABLE[datatype] if datatype in FORWARD_TABLE else FORWARD_TABLE[4]
		print("\tForwarded to", destination)
		client_sock.sendto(payload, (destination, UDP_PORT))
	except ConnectionError as e:
		print(e)