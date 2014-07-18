import socket

PROTOCOL_HEADER = 0x09F9

def read_protocol_packet(sock):
	header, addr = sock.recvfrom(2)
	if socket.ntohs(header) != PROTOCOL_HEADER:
		raise ConnectionError("Received invalid packet: Did not have proper protocol header")
	datatype = socket.recvfrom(2)[0] #discard source address
	length = ntohs(socket.recvfrom(2)[0])
	payload = socket.recvfrom(length)
	return (addr, datatype, payload)

def create_protocol_packet(datatype, payload):
	payload_bytes = bytes(payload)
	return sum(map(bytes, [ PROTOCOL_HEADER, datatype, htons(len(payload_bytes)), payload_bytes]))