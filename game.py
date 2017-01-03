import pygame
import random

from enum import Enum
from field import Field
	
class State(Enum):
	STOPPED   = 0
	RUNNING   = 1
	PAUSED    = 2
	GAME_OVER = 3

class Game:

	def __init__(self, width, height):
		self._state = State.RUNNING
		self._screen = pygame.display.set_mode((width, height))
		self._clock = pygame.time.Clock()
		self._clear_color = (64, 64, 64)
		self._scale = 20

		self._field = Field(height / self._scale, self._scale)

	def pause(self):
		self._state = State.PAUSED

	def unpause(self):
		if self._state != State.STOPPED and self._state != State.GAME_OVER:
			self._state = State.RUNNING

	def quit(self):
		self._state = State.STOPPED

	def update(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				self.quit()
				return
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_ESCAPE: 
					self.quit()
					return
				if event.key == pygame.K_SPACE:
					if self._state == State.RUNNING: self.pause()
					elif self._state == State.PAUSED: self.unpause()

		if self._state == State.RUNNING:
			self._field.update();

	def draw(self):
		self._screen.fill(self._clear_color)
		self._field.draw(self._screen)
		pygame.display.flip()

	def run(self):
		self._state = State.RUNNING
		while self._state != State.STOPPED:
			self.update()
			self.draw()
			self._clock.tick(60)
