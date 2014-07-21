import socket
import protocol

UDP_IP = "192.168.245.129"
UDP_PORT = 13337

sock = socket.socket(socket.AF_INET, #IP
	socket.SOCK_DGRAM) #UDP

while True:
	sock.sendto(create_protocol_packet(int(input("Datatype [0x0001]: " or "0x0001")),
		input("Payload [Test]: " or "Test"), 
		int(input("Protocol Header [0x09F9]: ") or "0x09F9")), (UDP_IP, UDP_PORT))