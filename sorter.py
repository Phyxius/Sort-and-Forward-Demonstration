import socket
from protocol import *
from util import *

FORWARD_TABLE = { "Text":"192.168.245.130", "Audio":"192.168.245.131", "Video":"192.168.245.132", "Other":"192.168.245.133" }

UDP_IP = "" #equivalent to IPADDR_ANY
UDP_PORT = 13337

server_sock = socket.socket(socket.AF_INET, #IP
	socket.SOCK_DGRAM) #UDP
server_sock.bind((UDP_IP, UDP_PORT))

#client_sock = socket.socket(socket.AF_INET, #IP
	#socket.SOCK_DGRAM) #UDP

log = open("sorter_log", "wb")

SOCK_TABLE = dict()
for key in FORWARD_TABLE:
	sock = socket.socket(socket.AF_INET, #IP
		socket.SOCK_DGRAM) #UDP
	sock.connect((FORWARD_TABLE[key], UDP_PORT))
	SOCK_TABLE[key] = sock

while True:
	try:
		source, datatype, payload = read_protocol_packet(server_sock)
		datatype = PROTOCOL_DATA_TYPES[datatype] if datatype in PROTOCOL_DATA_TYPES else datatype
		print("Received packet from {} with datatype {} and payload length {}".format(
			source[0] + ":" + str(source[1]), datatype, len(payload)))
		destination = SOCK_TABLE[datatype] if datatype in FORWARD_TABLE else FORWARD_TABLE["Other"]
		print("\tForwarded to", FORWARD_TABLE[datatype] if datatype in FORWARD_TABLE else FORWARD_TABLE["Other"])
		log.write(payload)
		log.flush()
		destination.sendall(payload)
	except ConnectionError as e:
		print(e)