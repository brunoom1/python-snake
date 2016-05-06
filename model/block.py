## block model
import pygame;
from object import Object

class Block(Object):
	sibling = False
	parent = False
	i = 0

	def __init__(self, parent, pos = (0,0), size = (20, 20)):
		self.parent = parent;
		Object.__init__(self, pos, size)

	def move(self, pos = ()):
		old_pos = (self.x, self.y);

		self.x = pos[0]
		self.y = pos[1]

		if(self.sibling):
			self.sibling.move(old_pos)


	def setSibling(self, block):
		self.sibling = block;


	def getSibling(self):
		return self.sibling

	def setParent(self, parent):
		self.parent = parent



	def paint(self, screen):
		
		if(self.parent):
			pygame.draw.rect(screen, [200,200,200], pygame.Rect( \
				self.x, \
				self.y, \
				self.width, \
				self.height))

			pygame.draw.rect(screen, [100,50,200], pygame.Rect( \
				self.x + 2, \
				self.y + 2, \
				self.width - 4, \
				self.height - 4))
		else:

			if(self.i == 0):
				self.i = 1
			else: 
				self.i = 0

			if(self.i == 0):
				pygame.draw.rect(screen, [200,200,200], pygame.Rect( \
					self.x, \
					self.y, \
					self.width, \
					self.height))

				pygame.draw.rect(screen, [100,50,200], pygame.Rect( \
					self.x + 2, \
					self.y + 2, \
					self.width - 4, \
					self.height - 4))
			else: 
				pygame.draw.rect(screen, [255,255,255], pygame.Rect( \
					self.x, \
					self.y, \
					self.width, \
					self.height))

				pygame.draw.rect(screen, [255,0,0], pygame.Rect( \
					self.x + 2, \
					self.y + 2, \
					self.width - 4, \
					self.height - 4))



