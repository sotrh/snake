import pygame
from collections import deque

def draw_snake(surface, snake, color, scale):
	for x, y in snake._body:
		pygame.draw.rect(surface, color, pygame.Rect(x * scale, y * scale, scale, scale))

class Snake:

	DIR_UP = 0
	DIR_DOWN = 1
	DIR_LEFT = 2
	DIR_RIGHT = 3

	_DIRECTIONS = {
		DIR_UP: (0, -1),
		DIR_DOWN: (0, 1),
		DIR_LEFT: (-1, 0),
		DIR_RIGHT: (1, 0)
	}

	def __init__(self, start_length, start_pos, start_direction):
		self._length = start_length
		self._body = deque([start_pos])
		self._direction = start_direction

		self.eat(start_length - 1)

	def eat(self, num_fruits):
		while num_fruits > 0:
			self._body.appendleft(self._body[0])
			num_fruits -= 1

	def move(self):
		next_pos = self.get_next_pos()
		self._body.append(next_pos)
		self._body.popleft()

	def valid_direction(self, direction):
		if direction == -1: return False
		if self._direction == Snake.DIR_UP and direction == Snake.DIR_DOWN: return False
		if self._direction == Snake.DIR_DOWN and direction == Snake.DIR_UP: return False
		if self._direction == Snake.DIR_LEFT and direction == Snake.DIR_RIGHT: return False
		if self._direction == Snake.DIR_RIGHT and direction == Snake.DIR_LEFT: return False

		return True

	def set_direction(self, direction):
		if self.valid_direction(direction):
			self._direction = direction

	def get_head(self):
		return self._body[-1]

	def get_tail(self):
		return self._body[0]

	def get_next_pos(self):
		vel = Snake._DIRECTIONS[self._direction]
		pos = self.get_head()

		return (pos[0] + vel[0], pos[1] + vel[1])