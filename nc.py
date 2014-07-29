import socket
import sys

sock = socket.socket(socket.AF_INET, #IP
	socket.SOCK_DGRAM) #UDP
sock.bind(("" if len(sys.argv) is 1 else sys.argv[1], 13337))

out = sys.stdout

while True:
	out.buffer.write(sock.recvfrom(4096)[0])
	out.flush()