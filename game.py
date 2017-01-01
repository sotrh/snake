import pygame

from snake import Snake
from snake import draw_snake

class Game:
	
	def __init__(self, width, height):
		self.running = False
		self.screen = pygame.display.set_mode((width, height))
		self.clock = pygame.time.Clock()
		self.clear_color = (0, 0, 0)

		self.frames_per_move = 10
		self.frames_passed = 0;
		self.snake = Snake(3, (0,0), Snake.DIR_RIGHT)
		self.snake_color = (255, 255, 0)
		self.desired_direction = -1

	def process_input(self):
		self.desired_direction = -1

		for event in pygame.event.get():
			if event.type == pygame.QUIT: self.running = False

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_ESCAPE: self.running = False

		keys = pygame.key.get_pressed()
		if keys[pygame.K_w]:
			self.desired_direction = Snake.DIR_UP
		if keys[pygame.K_s]:
			self.desired_direction = Snake.DIR_DOWN
		if keys[pygame.K_a]:
			self.desired_direction = Snake.DIR_LEFT
		if keys[pygame.K_d]:
			self.desired_direction = Snake.DIR_RIGHT

		if self.frames_passed > self.frames_per_move:
			self.snake.set_direction(self.desired_direction)
			self.snake.move()
			self.frames_passed = 0
		else: self.frames_passed += 1

	def draw(self):
		self.screen.fill(self.clear_color)

		draw_snake(self.screen, self.snake, self.snake_color, 20)

		pygame.display.flip()

	def run(self):
		self.running = True
		while self.running:
			self.process_input()
			self.draw()
			self.clock.tick(60)
