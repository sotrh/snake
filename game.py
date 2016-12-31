import pygame

class Game:
	
	def __init__(self, width, height):
		self.running = False
		self.screen = pygame.display.set_mode((width, height))
		self.clock = pygame.time.Clock()
		self.clear_color = (0, 0, 0)

	def process_input(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT: self.running = False
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_ESCAPE: self.running = False

	def draw(self):
		self.screen.fill(self.clear_color)
		pygame.display.flip()

	def run(self):
		self.running = True
		while self.running:
			self.process_input()
			self.draw()
			self.clock.tick(60)
