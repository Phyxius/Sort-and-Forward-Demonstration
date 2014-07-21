import socket
import binascii
import struct
from util import *

PROTOCOL_HEADER = 0x09F9
PROTOCOL_DATA_TYPES = { b'0001': "Text", b'0002': "Audio", b'0003': "Video", b'0004': "Other" }

def read_protocol_packet(sock):
	data, addr = sock.recvfrom(6, socket.MSG_PEEK)
	#print("received")
	if bytes_to_short(data[:2]) != PROTOCOL_HEADER:
		raise ConnectionError("Received invalid packet: Did not have proper protocol header (had '{}')".format(binascii.hexlify(header)))
	datatype = bytes_to_short(data[2:4])#discard source address
	length = bytes_to_short(data[4:])
	payload = sock.recv(6 + length)[6:]
	return (addr, datatype, payload)

def create_protocol_packet(datatype, payload, protocol_header = PROTOCOL_HEADER):
	payload_bytes = bytes(payload, "utf-8")
	return struct.pack(">hhh", protocol_header, datatype, len(payload_bytes)) + payload_bytes