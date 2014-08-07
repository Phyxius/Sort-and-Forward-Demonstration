#! /usr/bin/env python3
import socket

UDP_IP = "localhost"
UDP_PORT = 13337

sock = socket.socket(socket.AF_INET, #IP
	socket.SOCK_DGRAM) #UDP

while True:
	sock.sendto(bytes(input("Message: "), "utf-8"), (UDP_IP, UDP_PORT))