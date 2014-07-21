import struct

def bytes_to_short(bytes):
	return struct.unpack(">h", bytes)[0]
def short_to_bytes(short):
	return struct.pack(">h", short)

def default_input(prompt, default, append_default_and_colon = True):
	return input(prompt + (" [{}]: ".format(default) if append_default_and_colon else "")) or default