## snake model
from block import Block
from object import Object

class Snake(Object):

	directions = { 'top': 0, 'right': 1, 'bottom': 2, 'left': 3 }
	direct = directions['right']
	blocks = []

	def __init__(self, game = "", step = 20):
		Object.__init__(self, (0, 0), (0 , 0))
		self.game = game;
		self.step = step

	def move(self, direct = 0):

		if(self.direct == self.directions['top'] ):
			self.y -= self.step

			if(self.y < 0):
				self.y = self.game.size[1] - self.step

		if(self.direct == self.directions['right'] ):
			self.x += self.step;

			if(self.x + self.step > self.game.size[0]):
				self.x = 0

		if(self.direct == self.directions['bottom'] ):
			self.y += self.step;

			if(self.y + self.step > self.game.size[1]):
				self.y = 0

		if(self.direct == self.directions['left'] ):
			self.x -= self.step;

			if(self.x < 0 ):
				self.x = self.game.size[0] - self.step

		## move first block 
		if(len(self.blocks) > 0 and direct != 4): 
			self.blocks[0].move((self.x, self.y));

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
			self.setPos(block.getPos())
		else:
			self.blocks[total - 1].setSibling(block);
			self.blocks.append(block)

		block.setParent(block)

	def getBlocks(self):
		return self.blocks


	def paint(self, screen):

		for block in self.blocks:
			block.paint(screen);


if __name__ == "__main__":
	snake = Snake(False, 20)
	snake.addBlock(Block(snake, (0, 0), (20, 20)))
	snake.addBlock(Block(snake, (0,20), (20, 20)))
	snake.addBlock(Block(snake, (0,40), (20, 20)))

	snake.move(snake.directions['top']);
	snake.move(snake.directions['right']);
	snake.move(snake.directions['right']);
	snake.move(snake.directions['right']);
	# snake.move(snake.directions['bottom']);
	# snake.move(snake.directions['bottom']);
	# snake.move(snake.directions['bottom']);
	# snake.move(snake.directions['left']);

	i = 0;
	for block in snake.blocks:
		print i , "(" , block.x , "," , block. y , ")";
		i += 1;


