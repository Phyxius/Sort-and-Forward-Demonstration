import socket
import binascii
import struct
from util import *

PROTOCOL_HEADER_STRUCT_FORMAT = ">HHH"
PROTOCOL_HEADER = 0x09F9
PROTOCOL_DATA_TYPES = { 1: "Text", 2: "Audio", 3: "Video", 4: "Other" }

def read_protocol_packet(sock):
	data, addr = sock.recvfrom(6, socket.MSG_PEEK) #read first part of packet without allocating a large buffer or discarding the rest
	#print("received")
	header, datatype, length = struct.unpack(PROTOCOL_HEADER_STRUCT_FORMAT, data)
	if header != PROTOCOL_HEADER:
		sock.recv(1) #discard current packet
		raise ConnectionError("Received invalid packet: Did not have proper protocol header (had '0x%0.2X')" % header)
	payload = sock.recv(6 + length)[6:] #skip header
	return (addr, datatype, payload)

def create_protocol_packet(datatype, payload, protocol_header = PROTOCOL_HEADER):
	if payload is str:
		payload_bytes = bytes(payload, "utf-8")
	else:
		payload_bytes = payload
	return struct.pack(PROTOCOL_HEADER_STRUCT_FORMAT, 
		protocol_header, datatype, len(payload_bytes)) + payload_bytes