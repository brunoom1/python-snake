#coding: utf-8

import socket
import json

class Client:
	updates = []
	info = ()
	name = ""

	def __init__(self, client_info, client_id):
		self.id = client_id
		self.info = client_info
		self.name = "Player %s" % client_info[1]		

	def setUpdates(self, updates):
		self.updates = updates;

	def getUpdates(self):
		return self.updates

	def setName(self, name):
		self.name = name

	def getName(self):
		return self.name


class Server:

	clients = []
	max_clients = 5
	clients_updates = []

	def __init__(self, server_address):
		self.server_address = server_address
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

		self.sock.bind(server_address)

		print "Snake server iniciado"
		print "---------------------"

	def main(self):
		while True:
			msg = ""
			msg, client = self.sock.recvfrom(1024)

			if msg:
				client_in_list = False
				
				for cli in self.clients:
					if(cli.info == client):
						# cliente ja listado
						client_in_list = True

				if(not client_in_list):
					# se ainda tiver espaço, aloca cliente
					if(len(self.clients) < self.max_clients):
						print client, "client accepted"
						c = Client(client, int(client[1]));
						self.clients.append(c)
						self.sock.sendto(client[1].__str__(), client)

					else:
						self.sock.sendto('server-full', client)
				
				# se cliente estiver na lista
				else:

					decoder = json.decoder.JSONDecoder()
					encoder = json.encoder.JSONEncoder()

					#mensagens chegam no formato json e são decodificadas
					message = decoder.decode(msg);

					# se for um pedido para atualizar
					if message[0] == 'update':
						# client manda informações para o servidor
						for cli in self.clients:
							self.sock.sendto(msg, client)
							break


					elif message[0] == 'show-clients':
						names = []
						for cli in self.clients:
							names.append(cli.getName())

						self.sock.sendto(names.__str__(), client)


					elif message[0] == 'help':
						commands = ['set-update','get-updates','show-clients']
						self.sock.sendto(commands.__str__(), client)

						# mostra os clientes para o client especifico

					else:
						self.sock.sendto('Whats?', client)


	def __done__(self):
		self.sock.close()
