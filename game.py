import pygame
import random

from enum import Enum
from field import Field

pygame.init()
	
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
		self._width = width
		self._height = height

		# game over text
		self._font_game_over = pygame.font.Font(None, 30)
		self._label_game_over = self._font_game_over.render("Game Over!", True, (255, 255, 255))
		label_width, label_height = self._label_game_over.get_size()
		self._label_game_over_pos = (width / 2 - label_width / 2, height / 2 - label_height / 2)

		# continue text
		self._font_continue = pygame.font.Font(None, 20)
		self._label_contine = self._font_continue.render("Press [SPACE] to Play Again", True, (255, 255, 255))
		spacing = label_height + 10
		label_width, label_height = self._label_contine.get_size()
		self._label_contine_pos = (width / 2 - label_width / 2, height / 2 - label_height / 2 + spacing)

		self._field = Field(self, height / self._scale, self._scale)
		self._field_pos = \
			((width - self._field.get_scaled_size()) / 2, \
			 (height - self._field.get_scaled_size()) / 2)

	# state changing methods

	def pause(self):
		if self._state != State.GAME_OVER and self._state != State.STOPPED:
			self._state = State.PAUSED

	def unpause(self):
		if self._state != State.STOPPED and self._state != State.GAME_OVER:
			self._state = State.RUNNING

	def game_over(self):
		if self._state != State.STOPPED and self._state != State.PAUSED:
			self._state = State.GAME_OVER

	def quit(self):
		self._state = State.STOPPED

	def restart(self):
		del self._field
		del self._field_pos

		self._field = Field(self, self._height / self._scale, self._scale)
		self._field_pos = \
			((self._width - self._field.get_scaled_size()) / 2, \
			 (self._height - self._field.get_scaled_size()) / 2)

		self._state = State.RUNNING

	# update methods

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
					elif self._state == State.GAME_OVER: self.restart()

		if self._state == State.RUNNING:
			self._field.update();

	# draw methods

	def draw(self):
		self._screen.fill(self._clear_color)
		self._field.draw(self._screen, self._field_pos)

		if self._state == State.GAME_OVER:
			self._screen.blit(self._label_game_over, self._label_game_over_pos)
			self._screen.blit(self._label_contine, self._label_contine_pos)

		pygame.display.flip()

	# run method

	def run(self):
		self._state = State.RUNNING
		while self._state != State.STOPPED:
			self.update()
			self.draw()
			self._clock.tick(60)
