#!/usr/bin/python

import pygame
import model

from math import ceil
from random import random

class Game(pygame.Rect):

	speed = 8
	stage_blocks = []
	pause_game = True
	config = {}

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

		self.eventManager = model.EventManager(self);
		self.eventManager.start() 

		self.screenBuffer = pygame.Surface(self.size);

		self.snake.addBlock(model.Block(self.snake, (3 * block_s, 6 * block_s)) )
		self.snake.addBlock(model.Block(self.snake, (3 * block_s, 5 * block_s)) )
		self.snake.addBlock(model.Block(self.snake, (3 * block_s, 4 * block_s)) )
		self.snake.addBlock(model.Block(self.snake, (3 * block_s, 3 * block_s)) )
		self.snake.addBlock(model.Block(self.snake, (3 * block_s, 2 * block_s)) )

		# carrega primeiro stage
		self.load_stage(0, 20)


		block_free = False
		count = 0
		while(self.running):

			self.screenBuffer.fill([0,0,0])

			if(block_free == False):

				pos = ( int(random() * (self.size[0] / block_s)) * block_s , int(random() * (self.size[1] / block_s)) * block_s )
				block_free = model.Block(False, pos)

				while(block_free.collidelist(self.stage_blocks) != -1):
					pos = ( int(random() * (self.size[0] / block_s)) * block_s , int(random() * (self.size[1] / block_s)) * block_s )
					block_free = model.Block(False, pos)

			if(block_free != False):
				block_free.paint(self.screenBuffer)

				if(self.snake.blocks[0].colliderect(block_free)):
					self.snake.addBlock(block_free)
					block_free = False
					count += 1

					if(count % 5 == 0):
						self.speed += 1

					print count

			for block in self.stage_blocks:
				block.paint(self.screenBuffer)

			self.snake.paint(self.screenBuffer)

			# pass screenBuffer for real screen
			self.screen.blit(self.screenBuffer, (0, 0))

			# update display
			pygame.display.flip();

			if(self.pause_game): continue;


			# move snaker
			self.snake.move(self.snake.direct)

			# test collision

			index = self.snake.blocks[0].collidelist(self.stage_blocks)
			index2 = self.snake.blocks[0].collidelist(self.snake.blocks[1:-1])

			if index != -1 or index2 != -1:
				if(isinstance(self.stage_blocks[index], model.Brick)):
					self.running = False

			self.clock.tick(self.speed)


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
	game = Game((400, 400), 20)
