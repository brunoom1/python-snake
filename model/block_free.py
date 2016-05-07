## block model
import pygame;
import block;

class BlockFree(block.Block):
	sibling = False
	parent = False
	borderColor = [200,200,200]
	bgColor = [100,50,200]
	i = 0

	def __init__(self, parent, pos = (0,0), size = (20, 20)):
		self.parent = parent;
		block.Block.__init__(self,parent, pos, size)

	def paint(self, screen):
		
		if(self.i == 0):
			self.i = 1
		else: 
			self.i = 0

		if(self.i == 0):
			self.setBorderColor([200,200,200])
			self.setBgColor([100,50,200])
		else: 
			self.setBorderColor([200,200,200])
			self.setBgColor([255,0,0])

		block.Block.paint(self, screen);



