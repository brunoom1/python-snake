import json

## snake model
from block import Block
from object import Object

class Snake(Object):

	directions = { 'top': 0, 'right': 1, 'bottom': 2, 'left': 3 }
	direct = directions['right']
	blocks = []
	snake_id = 0

	def __init__(self, controller = "", step = 20):
		Object.__init__(self, (0, 0), (0 , 0))
		self.controller = controller;
		self.step = step
		self.snake_id = 0

	def setId(self, id):
		self.snake_id = id

	def getId(self):
		return self.snake_id

	def move(self, direct = -1):

		if(direct != -1):
			self.setDirect(direct)
		else: 
			if(self.direct == self.directions['top'] ):
				self.y -= self.step

				if(self.y < 0):
					self.y = self.controller.parent.size[1] - self.step

			if(self.direct == self.directions['right'] ):
				self.x += self.step;

				if(self.x + self.step > self.controller.parent.size[0]):
					self.x = 0

			if(self.direct == self.directions['bottom'] ):
				self.y += self.step;

				if(self.y + self.step > self.controller.parent.size[1]):
					self.y = 0

			if(self.direct == self.directions['left'] ):
				self.x -= self.step;

				if(self.x < 0 ):
					self.x = self.controller.parent.size[0] - self.step

			## move first block 
			if(len(self.blocks) > 0 and direct != 4): 
				self.blocks[0].move((self.x, self.y));

	def setPosition(self, x, y):
		self.x = x
		self.y = y
		self.blocks[0].move((self.x, self.y))

	def setDirect(self, direct):

		if( self.direct == self.directions['top'] 	 and direct != self.directions['bottom'] or \
			self.direct == self.directions['bottom'] and direct != self.directions['top'] or \
			self.direct == self.directions['left'] 	 and direct != self.directions['right'] or \
			self.direct == self.directions['right']  and direct != self.directions['left']):
			self.direct = direct

	def addBlock(self, block):
		total = len(self.blocks)
		if (total == 0):
			self.blocks.append(block)
			block.setParent(self);
		else:
			self.blocks[total - 1].setSibling(block);
			self.blocks.append(block)
		
		block.setParent(self.blocks[0]);


	def getBlocks(self):
		return self.blocks


	def paint(self, screen):

		for block in self.blocks:
			block.paint(screen);

	def setInfo(self, info):
		pass

	## retorna informacoes para ser udada no servidor
	def getInfo(self):

		infos = { \
			"id":self.getId(), \
			"pos": {"x": self.x, "y":self.y}, \
			"direction": self.direct, \
			"blocks-info": { \
				"bgcolor": self.blocks[0].getBgColor(), \
				"borderColor": self.blocks[0].getBorderColor(), \
				"blocksLen": len(self.blocks) \
			} \
		}


		return infos;


if __name__ == "__main__":
	snake = Snake(False, 20)
	snake.setId(38229)
	snake.addBlock(Block(snake, (0, 0), (20, 20)))
	snake.addBlock(Block(snake, (0,20), (20, 20)))
	snake.addBlock(Block(snake, (0,40), (20, 20)))

	print snake.getInfo();

