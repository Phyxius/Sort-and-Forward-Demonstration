import struct

def bytes_to_short(bytes):
	return struct.unpack(">h", bytes)[0]
def short_to_bytes(short):
	return struct.pack(">h", short)