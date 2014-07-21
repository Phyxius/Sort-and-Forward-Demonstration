import socket
import binascii
import struct
from util import *

PROTOCOL_HEADER = 0x09F9

def read_protocol_packet(sock):
	header, addr = sock.recvfrom(2)
	print("received")
	if bytes_to_short(header) != PROTOCOL_HEADER:
		raise ConnectionError("Received invalid packet: Did not have proper protocol header (had '{}')".format(binascii.hexlify(header)))
	datatype = sock.recvfrom(2)[0] #discard source address
	length = bytes_to_short(sock.recvfrom(2)[0])
	payload = sock.recvfrom(length)[0]
	return (addr, datatype, payload)

def create_protocol_packet(datatype, payload, protocol_header = PROTOCOL_HEADER):
	payload_bytes = bytes(payload, "utf-8")
	return struct.pack(">hhh", protocol_header, datatype, len(payload_bytes)) + payload_bytes