import socket
import binascii
from util import *

PROTOCOL_HEADER = 0x09F9

def read_protocol_packet(sock):
	header, addr = sock.recvfrom(2)
	if socket.ntohs(bytes_to_short(header)) != PROTOCOL_HEADER:
		raise ConnectionError("Received invalid packet: Did not have proper protocol header (had '{}')".format(binascii.hexlify(header)))
	datatype = socket.recvfrom(2)[0] #discard source address
	length = ntohs(bytes_to_short(socket.recvfrom(2)[0]))
	payload = socket.recvfrom(length)
	return (addr, datatype, payload)

def create_protocol_packet(datatype, payload, protocol_header = PROTOCOL_HEADER):
	payload_bytes = bytes(payload, "utf-8")
	return short_to_bytes(protocol_header) + short_to_bytes(datatype) + short_to_bytes(socket.htons(len(payload_bytes))) + payload_bytes