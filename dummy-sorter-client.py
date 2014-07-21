import socket
import binascii
from protocol import create_protocol_packet

UDP_IP = "192.168.245.129"
UDP_PORT = 13337

sock = socket.socket(socket.AF_INET, #IP
	socket.SOCK_DGRAM) #UDP

while True:
	packet = create_protocol_packet(int(input("Datatype [0x0001]: ") or "0x0001", 16),
		input("Payload [Test]: ") or "Test", 
		int(input("Protocol Header [0x09F9]: ") or "0x09F9", 16))
	sock.sendto(packet, (UDP_IP, UDP_PORT))
	print("Sent packet:", binascii.hexlify(packet))