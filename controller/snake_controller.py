#coding: utf-8

""" Módulo SnakeController """

import model
import view

class SnakeController:
	""" Esta classe tem como finalidade realizar o controle do snake no jogo, a ideia de se ter um controle
		ao invés de controlar diretamente o objeto modelo, é poder entregar este controle a qualquer
		objeto capas de controlalo como por exemplo um servidor """

	parent = False

	def __init__(self, parent):
		self.view = view.SnakeView(self);
		self.parent = parent
				
		self.snake = model.Snake(self, parent.DEFAULT_BLOCK_SIZE)
		self.snake.addBlock(model.Block(self.snake))
		self.snake.addBlock(model.Block(self.snake))
		self.snake.addBlock(model.Block(self.snake))
		self.snake.addBlock(model.Block(self.snake))
		self.snake.addBlock(model.Block(self.snake))


	def getView(self):
		return self.view

	def verifyCollision(self):
		
		## verificar colisão com o block_free
		block_free = self.parent.blockFreeController.block;
		if(block_free != False):
			if(block_free.colliderect(self.snake)):
				# muda o objeto para instancia de block
				block_free.toBlock()				
				self.snake.addBlock(block_free)
				self.parent.blockFreeController.block = False


	def move(self, direction = -1):
		self.snake.move(direction)
		pass

	def update(self):
		self.move() # move snake a cada interação
		self.verifyCollision()
		self.view.render(self.snake)
