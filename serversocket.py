#!/usr/bin/python3
# This script is to Create server socket.and mirror the text which are send by client

import socket

TCPSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
TCPSocket.bind(("0.0.0.0",9001))
#print("TCPSocket binded")
TCPSocket.listen()
print("Waiting for Client...")
(ClientSocket,(ip,port))=TCPSocket.accept()
print("Received connection from:",ip )
#data=ClientSocket.recv(4096)
print("Start echo output...")

while True:
	data=ClientSocket.recv(4096)
	if not data:
		break
	print(data)
	ClientSocket.send(data)
print("Closing connection ...\nShutting down server ...")
ClientSocket.close()
TCPSocket.close()


