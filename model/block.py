## block model
import pygame;
from object import Object

class Block(Object):
	sibling = False
	parent = False
	borderColor = [200,200,200]
	bgColor = [100,50,200]

	i = 0

	def __init__(self, parent, pos = (0,0), size = (20, 20)):
		self.parent = parent;
		Object.__init__(self, pos, size)

	def setBorderColor(self, borderColor):
		self.borderColor = borderColor

	def setBgColor(self, bgColor):
		self.bgColor = bgColor

	def getBgColor(self):
		return self.bgColor

	def getBorderColor(self):
		return self.borderColor

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
		
		pygame.draw.rect(screen, self.borderColor, pygame.Rect( \
			self.x, \
			self.y, \
			self.width, \
			self.height))

		pygame.draw.rect(screen, self.bgColor, pygame.Rect( \
			self.x + 2, \
			self.y + 2, \
			self.width - 4, \
			self.height - 4))


