#!/usr/bin/python

import pygame
import model

from math import ceil
from random import random

class Game(pygame.Rect):

	speed = 10
	stage_blocks = []

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

		self.snake.addBlock(model.Block(self.snake, (0, 0)) )
		self.snake.addBlock(model.Block(self.snake, (0, 0)) )
		self.snake.addBlock(model.Block(self.snake, (0, 0)) )
		self.snake.addBlock(model.Block(self.snake, (0, 0)) )
		self.snake.addBlock(model.Block(self.snake, (0, 0)) )

		self.eventManager = model.EventManager(self);
		self.eventManager.start() 

		self.offset = pygame.Surface(self.size);

		# carrega primeiro stage
		self.load_stage(0, 20)

		block_free = False
		while(self.running):

			if(block_free == False):

				pos = ( int(random() * (self.size[0] / block_s)) * block_s , int(random() * (self.size[1] / block_s)) * block_s )
				block_free = model.Block(False, pos)

				while(block_free.collidelist(self.stage_blocks) != -1):
					pos = ( int(random() * (self.size[0] / block_s)) * block_s , int(random() * (self.size[1] / block_s)) * block_s )
					block_free = model.Block(False, pos)


			self.offset.fill([0,0,0])
			self.snake.move(self.snake.direct)
			self.snake.paint(self.offset)

			if(block_free != False):
				block_free.paint(self.offset)

				if(self.snake.blocks[0].colliderect(block_free)):
					self.snake.addBlock(block_free)
					block_free = False

			for block in self.stage_blocks:
				block.paint(self.offset)

			index = self.snake.blocks[0].collidelist(self.stage_blocks)
			index2 = self.snake.blocks[0].collidelist(self.snake.blocks[1:-1])

			if index != -1 or index2 != -1:
				if(isinstance(self.stage_blocks[index], model.Brick)):
					self.running = False

			self.screen.blit(self.offset, (0, 0))

			pygame.display.flip();
			self.clock.tick(self.speed)


	def __done__(self):
		pygame.quit()


	def load_stage(self, stage_number, block_s):
		file_name = "stages/stage%d" % (stage_number)

		f = file(file_name)
		content = f.read();
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
