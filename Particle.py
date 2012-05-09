import pygame
from math import cosin, sin, pi, sqrt, pow
from random import random, uniform

class Target(object):
	def __init__(self):
		self.size = 2 * (uniform(1,3))
		self.x = 462
		self.y = 273
		self.speed = 0
		self.angle = uniform(0, pi * 2)
		self.speed = random()
		self.surf = pygame.image.load("particle.png").convert()
		self.surf = pygame.transform.smoothscale(self.surf, (size,size))
		self.rect = self.surf.get_rect()
		self.screen = pygame.display.get_surface()
		self.distance = 0
	
	def update(self):
		self.x += sin(self.angle) * self.speed
		self.y -= cos(self.angle) * self.speed
		self.distance = sqrt(pow(self.x - 462,2) + pow(self.y - 273,2))
		self.surf = pygame.transform.smoothscale(self.surf, (2.71828*self.size, 2.71828*self.size)