#coding: utf-8
import threading
import pygame

import socket
import sys
import json

import controller


## rodar evento fora do loop principal do sistema
class ServerComunicate(threading.Thread):

	def __init__(self, parent):
		self.parent = parent
		threading.Thread.__init__(self);

		self.server_address = ('127.0.0.1', 8765)

	def run(self):

		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

		print "server comunicate"

		self.sock.sendto("hello", self.server_address)

		msg_server, address = self.sock.recvfrom(1024)
		game_id = 0

		if(msg_server == "server-full"):
			print "Server is fulling, return back tomorrow"
			self.parent.running = False
		else:
			game_id = int(msg_server)

		if(game_id):
			self.parent.game_id = game_id;
			self.parent.snakeController.snake.setId(game_id)
		
		countComunication = 0

		## controllers que serao 
		self.snakeControllers = [];

		while(self.parent.running):
			# manda as informações
			encoder = json.encoder.JSONEncoder()
			decoder = json.decoder.JSONDecoder()

			# send server msg
			msg = encoder.encode(['update', {'snake': self.parent.snakeController.snake.getInfo()}]);
			self.sock.sendto(msg, self.server_address)

			msg, address = self.sock.recvfrom(1024);
			msg = decoder.decode(msg);

			if(msg[0] == "update"):
				# get server other clients update

				msg_client_id = int(msg[1]['snake']['id'])
				if(msg_client_id <= 0):
					continue

				# ve se tem controle para todos os clientes se nao tiver cria
				achou = False
				for ctrl in self.snakeControllers:
					# achou um controller para o id
					if ctrl.snake.getId() == msg_client_id:
						achou = True
						break
				
				if(not achou):
					## adiciono novo controller para o id
					new_controller = controller.SnakeController(self.parent)
					self.parent.controllers.append(new_controller)
					self.snakeControllers.append(new_controller)


			countComunication += 1
