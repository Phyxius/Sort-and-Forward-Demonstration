import socket
import binascii
import struct
from util import *

PROTOCOL_HEADER_STRUCT_FORMAT = ">HHH"
PROTOCOL_HEADER = 0x09F9 #cookie for you if you recognize this number
PROTOCOL_DATA_TYPES = { 0x11: "Text", 0x22: "Audio", 0x33: "Video", 0x44: "Other" }

def read_protocol_packet(sock):
	data, addr = sock.recvfrom(6, socket.MSG_PEEK) #read first part of packet without allocating a large buffer or discarding the rest
	header, datatype, length = struct.unpack(PROTOCOL_HEADER_STRUCT_FORMAT, data)
	if header != PROTOCOL_HEADER:
		sock.recv(1) #bad packet, discard
		raise ConnectionError("Received invalid packet: Did not have proper protocol header (had '0x%0.2X')" % header)
	payload = sock.recv(length + 6)[6:] #skip header
	return (addr, datatype, payload)

def create_protocol_packet(datatype, payload, protocol_header = PROTOCOL_HEADER):
	if payload is str:
		payload_bytes = bytes(payload, "utf-8")
	else:
		payload_bytes = payload
	return struct.pack(PROTOCOL_HEADER_STRUCT_FORMAT, 
		protocol_header, datatype, len(payload_bytes)) + payload_bytes