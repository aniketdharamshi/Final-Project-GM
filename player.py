import pygame, sys, os
import random

class Player(object):
	def __init__(self):
		self.surf = pygame.transform.smoothscale(pygame.image.load("player.png").convert_alpha(), (30,30))
		self.rect = self.surf.get_rect()
	def update(self):
		x = self.TransferX()
		y = self.TransferY()
		self.rect.center = (x, y)
		if self.rect.bottom > 600:
			self.rect.bottom = 600
		if self.rect.right > 900:
			self.rect.right = 900
	def TransferX(self):
		self.cursor = pygame.mouse.get_pos()
		self.x = self.cursor[0]
		self.transformer = 0.2
		self.x_final = ((1-(0.9 *self.transformer)) * self.x)
		return self.x_final
	def TransferY(self):
		self.cursor = pygame.mouse.get_pos()
		self.y = self.cursor[1]
		self.transformer = 0.2
		self.y_final = ((1-(0.9 *self.transformer)) * self.y)
		return self.y_final