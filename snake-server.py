#!/usr/bin/python 
from lib import Server

server_address = ('localhost', 8765)
server = Server(server_address)
server.main()