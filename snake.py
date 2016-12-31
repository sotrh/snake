from collections import deque

class Snake:

	DIR_UP = 0
	DIR_DOWN = 1
	DIR_LEFT = 2
	DIR_RIGHT = 3

	_DIRECTIONS = {
		DIR_UP: (0, 1),
		DIR_DOWN: (0, -1),
		DIR_LEFT: (-1, 0),
		DIR_RIGHT: (1, 0)
	}

	def __init__(self, start_length, start_pos, start_direction):
		self._length = start_length
		self._body = deque([start_pos])
		self._direction = start_direction

		eat(start_length - 1)

	def eat(self, num_fruits):
		while num_fruits > 0:
			self.body.append(self.body[0])
			num_fruits -= 1

	def move(self):
		vel = _DIRECTIONS[self._direction]
		pos = self._body[-1]
		self._body.append((pos[0] + vel[0], pos[1] + vel[1]))