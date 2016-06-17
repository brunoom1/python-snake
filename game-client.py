#!/usr/bin/python
#coding: utf-8

import pygame
import model

from math import ceil
from random import random

import socket
import sys
import json

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('127.0.0.1', 8765)

sock.sendto("hello", server_address)
msg_server, address = sock.recvfrom(1024)
game_id = 0

if(msg_server == "server-full"):
	print "Server is fulling, return back tomorrow"
	sys.exit()
else:
	game_id = int(msg_server)


class Game(pygame.Rect):

	speed = 8
	stage_blocks = []
	pause_game = True
	config = {}
	snakes = []

	def __init__(self, size, block_s, winstyle=0):

		pygame.init()

		## init
		pygame.Rect.__init__(self, (0, 0) , (size[0], size[1]))

		## init windows
		self.winstyle = winstyle
		bestdepth = pygame.display.mode_ok(self.size, self.winstyle, 32)
		self.screen = pygame.display.set_mode(self.size, self.winstyle, bestdepth)

		## init and running
		self.running = True
		self.clock = pygame.time.Clock()
		
		self.snake = model.Snake(self, block_s)
		self.snake.setId(game_id)

		self.eventManager = model.EventManager(self);
		self.eventManager.start() 

		self.screenBuffer = pygame.Surface(self.size);

		self.snake.addBlock(model.Block(self.snake, (3 * block_s, 6 * block_s)) )
		self.snake.addBlock(model.Block(self.snake, (3 * block_s, 5 * block_s)) )
		self.snake.addBlock(model.Block(self.snake, (3 * block_s, 4 * block_s)) )
		self.snake.addBlock(model.Block(self.snake, (3 * block_s, 3 * block_s)) )
		self.snake.addBlock(model.Block(self.snake, (3 * block_s, 2 * block_s)) )

		self.snakes.append(self.snake);

		# load stage
		self.load_stage(0, 20)


		block_free = False
		count = 0
		while(self.running):

			self.update()

			self.screenBuffer.fill([0,0,0])

			if(block_free == False):

				pos = ( int(random() * (self.size[0] / block_s)) * block_s , int(random() * (self.size[1] / block_s)) * block_s )
				block_free = model.BlockFree(False, pos)

				while(block_free.collidelist(self.stage_blocks) != -1):
					pos = ( int(random() * (self.size[0] / block_s)) * block_s , int(random() * (self.size[1] / block_s)) * block_s )
					block_free = model.BlockFree(False, pos)

			for snake in self.snakes:

				if(block_free != False):
					block_free.paint(self.screenBuffer)

					if(snake.blocks[0].colliderect(block_free)):
						snake.addBlock(model.Block([], block_free.getPos()))
						block_free = False

				for block in self.stage_blocks:
					block.paint(self.screenBuffer)

				snake.paint(self.screenBuffer)

				# pass screenBuffer for real screen
				self.screen.blit(self.screenBuffer, (0, 0))

				# update display
				pygame.display.flip();

				if(self.pause_game): continue;


				# move snaker
				snake.move(snake.direct)

				# test collision

				index = snake.blocks[0].collidelist(self.stage_blocks)
				index2 = snake.blocks[0].collidelist(self.snake.blocks[1:-1])

				if index != -1 or index2 != -1:
					if(isinstance(self.stage_blocks[index], model.Brick)):
						self.running = False

			self.clock.tick(self.speed)

		# endwhile

	def update(self):
		# manda as informações
		encoder = json.encoder.JSONEncoder()
		decoder = json.decoder.JSONDecoder()

		msg = encoder.encode(['set-update', {'snake': self.snake.getInfo()}]);
		sock.sendto(msg, server_address)

		# get updates
		updates = []
		msg = encoder.encode(['get-updates']);
		sock.sendto(msg, server_address)

		# get 
		updates, address = sock.recvfrom(1024)
		update = decoder.decode(updates)
		total = int(update['total']); 

		if(total > 0):
			i = 0
			while( i < total):
				update, address = sock.recvfrom(1024)
				info = decoder.decode(update);
				encontrou = False

				for snake in self.snakes:
					if(snake.getId() == info["snake"]["id"] ):
						encontrou = True
						snake.setInfo(info["snake"])
						break

				if(not encontrou):
					snake = model.Snake(self, 20);
					snake.setInfo(info["snake"])
					self.snakes.append(snake)			
					print self.snakes	

				i += 1


	def __done__(self):
		pygame.quit()


	def load_stage(self, stage_number, block_s):
		file_name = "stages/stage%d" % (stage_number)

		########################################################################
		# linha 1 - snake init: posx, posy, direction, total blocks init #
		# linha 2 - speed game
		# linha > 2 - map elements
		#
		########################################################################

		f = file(file_name)

		line1 = f.readline().split(',')
		line2 = f.readline().split(',')

		self.config['snake'] = line1
		self.config['game'] = line2

		content = f.read()
		f.close()

		#  @ -> brick
		x = 0
		y = 0
		i = 0
		while i < len(content):
			ch = content[i]

			if(ch == "@"):
				self.stage_blocks.append(model.Brick(self, (x * block_s, y * block_s), (block_s, block_s))) 

			x += 1
			
			if(ch == '\n'):
				y += 1
				x = 0

			i += 1


## init game
if __name__ == '__main__': 
	game = Game((500, 500), 20)
