import pygame
class Body:
	def __init__(self, position, radius, screen):
		self.position = position
		self.radius = radius
		self.screen = screen
		self.done = False
		self.color = (255,255,255)

	def draw(self):
		pygame.draw.circle(self.screen, self.color , self.position, self.radius)

	def enlarge(self):
		self.radius += 1

	def finish(self):
		self.color = (255,0,0)
		self.done = True