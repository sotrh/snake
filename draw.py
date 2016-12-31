import pygame
from snake import Snake

def draw_snake(surface, snake, color, scale):
	for x, y in snake._body:
		pygame.draw.rect(surface, color, pygame.Rect(x * scale, y * scale, scale, scale))
