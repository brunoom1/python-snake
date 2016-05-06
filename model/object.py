import pygame

class Object(pygame.Rect):

	def __init__(self, pos, size):
		pygame.Rect.__init__(self, pos, size)

	def move(self, pos):
		self.x = pos[0]
		self.y = pos[1]

	def setPos(self, pos):
		self.x = pos[0]
		self.y = pos[1]

	def getPos(self):
		return (self.x, self.y)
