import pygame
from math import sin, cos, pi
from random import uniform, randrange

class Target(object):
	def __init__(self):
		self.size = 2 * (randrange(32,34,4))
		self.x = 462
		self.y = 273
		self.speed = 1
		self.angle = uniform(0, pi * 2)
		self.surf = pygame.image.load("particle.png").convert()
		self.surf = pygame.transform.smoothscale(self.surf, (self.size,self.size))
		self.rect = self.surf.get_rect()
		self.rect.center = (462,273)
		self.screen = pygame.display.get_surface()
		self.distance = 0
	
	def update(self):
		print(self.rect.width)
		self.x += round(sin(self.angle) * self.speed + .5)
		self.y -= round(cos(self.angle) * self.speed + .5)
		self.rect.center = (self.x, self.y)
		self.distance = sqrt(pow(self.x - 462,2) + pow(self.y - 273,2))
		self.surf = pygame.transform.smoothscale(self.surf, (4 * 2.71828*self.size, 4 * 2.71828*self.size))
		self.rect = self.rect.inflate((4 * 2.71828*self.size, 4 * 2.71828*self.size))