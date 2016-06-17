#!/usr/bin/python
import socket
import sys
import json

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('127.0.0.1', 8765)

sock.sendto("hello", server_address)
msg_server, address = sock.recvfrom(1024)

if(msg_server == "server-full"):
	print "Server is fulling, return back tomorrow"
	sys.exit()
else:
	print msg_server

msg = raw_input("")
while(True):

	# send menssage to server
	msg = json.dumps(msg.split(','));
	sock.sendto(msg, server_address)

	print "- Send: ", msg

	# aguarda resposta
	msg_server, address = sock.recvfrom(4000)
	if(msg_server):
		print "- Server: ", msg_server, address

	# manda outra mensagem
	msg = raw_input("");

sock.close()

