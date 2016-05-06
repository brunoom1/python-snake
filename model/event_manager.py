import threading
import pygame

## rodar evento fora do loop principal do sistema
class EventManager(threading.Thread):
	def __init__(self, game):
		self.game = game

		threading.Thread.__init__(self);

	def run(self):

		while(self.game.running):
			evt = pygame.event.wait();

			if(evt.type == pygame.QUIT):
				self.game.running = False

			if evt.type == pygame.KEYDOWN:

				if(evt.key == 273):
					self.game.snake.setDirect(0);
				elif( evt.key == 275 ):
					self.game.snake.setDirect(1);
				elif( evt.key == 274):
					self.game.snake.setDirect(2);
				elif( evt.key == 276):
					self.game.snake.setDirect(3);
