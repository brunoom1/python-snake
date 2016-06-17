
class SnakeView:
	snake = ""
	controller = ""

	def __init__(self, controller):
		self.controller = controller

	def render(self, snake):
		snake.paint(self.controller.parent.screenBuffer)		

