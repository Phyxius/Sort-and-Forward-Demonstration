import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 13337

sock = socket.socket(socket.AF_INET, #IP
	socket.SOCK_DGRAM) #UDP

while True:
	sock.sendto(input("Message: "), (UDP_IP, UDP_PORT))