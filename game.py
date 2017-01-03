import pygame
import random


from field import Field

class Game:
	
	def __init__(self, width, height):
		self._running = False
		self._screen = pygame.display.set_mode((width, height))
		self._clock = pygame.time.Clock()
		self._clear_color = (0, 0, 0)
		self._scale = 20

		self._field = Field(height / self._scale, self._scale)

	def update(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT: self._running = False

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_ESCAPE: self._running = False

		self._field.update();

	def draw(self):
		self._screen.fill(self._clear_color)
		self._field.draw(self._screen)
		pygame.display.flip()

	def run(self):
		self._running = True
		while self._running:
			self.update()
			self.draw()
			self._clock.tick(60)
