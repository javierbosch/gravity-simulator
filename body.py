import pygame
import math
velocity_constant = 50

class Body:

	def __init__(self, position, radius, screen):
		self.position = position
		self.radius = radius
		self.mass = (4/3) * math.pi * (self.radius**3)
		self.screen = screen
		self.done = False
		self.color = (255,255,255)
		self.forces = (0.0,0.0)

	def draw(self):
		pygame.draw.circle(self.screen, self.color , self.position, self.radius)

	def enlarge(self):
		self.radius += 1
		self.mass = (4/3) * math.pi * (self.radius**3)

	def finish(self, mouse_position):
		self.color = (255,0,0)
		self.velocity = tuple(map(lambda i, j: (i - j)//velocity_constant, self.position, mouse_position)) 
		self.mass = (4/3) * math.pi * (self.radius**3)
		self.done = True
	
	def move(self):
		self.position = tuple(map(lambda i, j: int (i + j), self.position, self.velocity)) 
		a = tuple(map(lambda i: i/self.mass, self.forces)) 
		self.velocity = tuple(map(lambda i, j: i + j, self.velocity, a))
		self.forces = (0.0,0.0)

	def collision(self,other):
		distance = math.sqrt( ((self.position[0] - other.position[0])**2) + ((self.position[1] - other.position[1])**2) )
		total_radiuus = self.radius + other.radius
		return distance<total_radiuus

	def collided_body(self,other,another):
		self.color = (0,255,0)
		self.mass = other.mass + another.mass
		self.position = tuple(map(lambda i, j: int ((i*other.mass + j*another.mass)/ self.mass) , other.position, another.position))
		self.radius =  (int(round((((3/4) * self.mass)/math.pi)  ** (1. / 3))))
		self.velocity = (0.0,0.0)
		self.done = True