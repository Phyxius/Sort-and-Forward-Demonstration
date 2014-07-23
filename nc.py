import socket
import sys

sock = socket.socket(socket.AF_INET, #IP
	socket.SOCK_DGRAM) #UDP
sock.bind(("", 13337))

out = sys.stdout

while True:
	out.buffer.write(sock.recv(2**16))
	out.flush()