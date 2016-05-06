import block;
import pygame

class Brick(block.Block):

	def __init__(self, parent, pos=(0,0), size=(0,0)):
		block.Block.__init__(self, parent, pos, size)

	def paint(self, screen):
		pygame.draw.rect(screen, [200,200,200], pygame.Rect( \
			self.x, \
			self.y, \
			self.width, \
			self.height))

		pygame.draw.rect(screen, [100,100,100], pygame.Rect( \
			self.x + 2, \
			self.y + 2, \
			self.width - 4, \
			self.height - 4))




