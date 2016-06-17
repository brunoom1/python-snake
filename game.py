#!/usr/bin/python
#coding: utf-8

import pygame

# mvc
import controller
import model

from math import ceil

import socket
import sys
import json

import lib


class Game(pygame.Rect):

	DEFAULT_BLOCK_SIZE = 20

	speed = 8
	stage_blocks = []
	pause_game = True
	game_id = 0
	config = {}

	def __init__(self, size, block_s, winstyle=0):


		pygame.init()

		self.block_s = block_s;

		self.controllers = []

		## init
		pygame.Rect.__init__(self, (0, 0) , (size[0], size[1]))

		## init windows
		self.winstyle = winstyle
		bestdepth = pygame.display.mode_ok(self.size, self.winstyle, 32)

		## surfaces 
		self.screen = pygame.display.set_mode(self.size, self.winstyle, bestdepth)
		self.screenBuffer = pygame.Surface(self.size);

		## init and running
		self.running = True
		self.clock = pygame.time.Clock()
		
		self.snakeController = controller.SnakeController(self)
		self.blockFreeController = controller.BlockFreeController(self)

		self.controllers.append(self.snakeController)
		self.controllers.append(self.blockFreeController)

		self.eventManager = model.EventManager(self.snakeController)
		self.eventManager.start() 

		self.serverComunicate = lib.ServerComunicate(self)
		self.serverComunicate.start()

		# contador de iterações
		count = 0
		while(self.running):
			# apaga tudo
			self.eraser()

			# atualiza
			self.update()			

			# pinta
			self.paint()

			# atrasa um certo tempo
			self.clock.tick(self.speed)

	def eraser(self):
		self.screenBuffer.fill([0,0,0])

	def update(self):
		# update controllers
		for control in self.controllers:
			control.update()

	def paint(self):
		# pass screenBuffer for real screen
		self.screen.blit(self.screenBuffer, (0, 0))

		# update display
		pygame.display.flip();


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
		# self.config['game'] = line2

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
	game = Game((400, 400), Game.DEFAULT_BLOCK_SIZE)
