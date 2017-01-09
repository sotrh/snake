import pygame
import random
from pygame import Surface
from snake import Snake
from snake import draw_snake

class Field:

	def __init__(self, game, size, scale):
		self._game = game
		self._size = size
		self._scale = scale

		self._surface = Surface((self._size * self._scale, self._size * self._scale)).convert()
		self._clear_color = (0, 0, 0)

		self._frames_per_update = 10
		self._frames_passed = 0

		self._desired_direction = Snake.DIR_RIGHT
		self._snake = Snake(3, (0, 0), self._desired_direction)
		self._snake_color = (255, 255, 0)

		self._fruit_dict = {}
		self._max_fruits = 3
		self._fruit_collected = 0
		self._chance_to_spawn_fruit = 0.1

	def __contains__(self, pos):
		x, y = pos
		return 0 <= x < self._size and 0 <= y < self._size

	def update(self):
		self.process_input()

		if self._frames_passed >= self._frames_per_update:
			self._frames_passed = 0
			self.spawn_fruit()
			self.move_snake()
		else:
			self._frames_passed += 1

	def process_input(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_w]:
			self._desired_direction = Snake.DIR_UP
		if keys[pygame.K_s]:
			self._desired_direction = Snake.DIR_DOWN
		if keys[pygame.K_a]:
			self._desired_direction = Snake.DIR_LEFT
		if keys[pygame.K_d]:
			self._desired_direction = Snake.DIR_RIGHT

	def spawn_fruit(self):
		if len(self._fruit_dict) < self._max_fruits \
			and random.random() < self._chance_to_spawn_fruit:
			pos = (random.randrange(self._size), random.randrange(self._size))

			while pos in self._fruit_dict or pos in self._snake:
				pos = (random.randrange(self._size), random.randrange(self._size))

			self._fruit_dict[pos] = 1 # bigger numbers = more snake length	

	def move_snake(self):
		self._snake.set_direction(self._desired_direction)
		next_pos = self._snake.get_next_pos()

		# assert that the snake can move forward
		if not (next_pos in self) or next_pos in self._snake:
			self._game.game_over()
			return

		# determine if moving will consume a fruit
		if next_pos in self._fruit_dict:
			self._snake.eat(self._fruit_dict[next_pos])
			del self._fruit_dict[next_pos]

		# actually move
		self._snake.move()

	def draw(self, screen, pos):
		self._surface.fill(self._clear_color)
		self.draw_fruit()
		draw_snake(self._surface, self._snake, self._snake_color, self._scale)

		screen.blit(self._surface, pos)

	def draw_fruit(self):
		for x, y in self._fruit_dict:
			pygame.draw.rect(self._surface, (255, 0, 0), pygame.Rect(x * self._scale, y * self._scale, self._scale, self._scale))

	def get_scaled_size(self):
		return self._size * self._scale