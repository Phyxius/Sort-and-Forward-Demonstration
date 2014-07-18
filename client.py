#! /usr/bin/env python3
import socket

UDP_IP = "192.168.245.129"
UDP_PORT = 13337

sock = socket.socket(socket.AF_INET, #IP
	socket.SOCK_DGRAM) #UDP

while True:
	sock.sendto(bytes(input("Message: "), "utf-8"), (UDP_IP, UDP_PORT))