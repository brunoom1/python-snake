import threading
import pygame

## rodar evento fora do loop principal do sistema
class EventManager(threading.Thread):

	def __init__(self, controller):
		self.controller = controller
		threading.Thread.__init__(self);

	def run(self):

		while(self.controller.parent.running):
			evt = pygame.event.wait();

			if(evt.type == pygame.QUIT):
				self.controller.parent.running = False

			if evt.type == pygame.KEYDOWN:

				if(evt.key == 273):
					self.controller.move(0);
				elif( evt.key == 275 ):
					self.controller.move(1);
				elif( evt.key == 274):
					self.controller.move(2);
				elif( evt.key == 276):
					self.controller.move(3);

				if(self.controller.parent.pause_game and evt.key == 32):
					self.controller.parent.pause_game = False;
