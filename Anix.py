import sys
import random
import math
import os
import getopt
import pygame
from socket import *
from pygame.locals import *

black = [0, 0, 0]
white = [255, 255, 255]
red = [255, 0, 0]
gray = [255, 0, 0]
screen = pygame.display.set_mode((900,600))

class Particle:
	def __init__(self, (x, y), size):
		self.x = x
		self.y = y
		self.size = size
		self.colour = (255, 255, 255)
		self.thickness = 2
		self.speed = 0
		self.angle = 0
		self.image = pygame.image.load("blue.gif").convert()
		self.image = pygame.transform.scale(self.image, (size))
		self.rect = self.image.get_rect()
		self.screen = pygame.display.get_surface()
	
	def move(self):
		self.x += math.sin(self.angle) * self.speed
		self.y -= math.cos(self.angle) * self.speed

class Ship(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("player.png").convert()
		self.image = pygame.transform.scale(self.image, (30, 30))
		self.rect = self.image.get_rect()
                screen = pygame.display.get_surface()
	def update(self):
		cursor = pygame.mouse.get_pos()
		x = cursor[0]
		y = cursor[1]
		return [x, y]
		
class Game(object):
	def __init__(self):
		self.game_over = False
		self.Clock = pygame.time.Clock()
	
	def process_input(self):
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					self.game_over = True
	def update(self):
		pass
	def draw(self, newpos):
		ship.rect.topleft = (newpos)
		self.screen.blit(player.image, (newpos))
		
def main():
	 # Initialise screen
        pygame.init()
        screen = pygame.display.set_mode((900, 600))
	background = pygame.image.load("background.jpg").convert()
	back = pygame.Surface(screen.get_size())
	render = pygame.sprite.Group()
	screen.blit(background, (0, 0))
	g = Game()
	ship = Ship()
	clock = pygame.time.Clock()
	size = random.randint (7, 10)
	p_size = ((2 * size),(2 * size))
	number_of_particles = 10
	my_particles = []
	for n in range(number_of_particles):
		size = random.randint(7, 10)
		p_size = ((5 * size),(5 * size))
		
		particle = Particle((462, 273), p_size)
		particle.speed = random.random()
		particle.angle = random.uniform(0, math.pi*2)
		
		my_particles.append(particle)
		
	running = True
	while running:
	    for event in pygame.event.get():
		if event.type == pygame.QUIT:
		    running = False
		screen.fill(black)
		screen.blit(background, (0, 0))
		g.process_input()
		g.update()
		newpos = ship.update()
		ship.rect.topleft = (newpos)
		ship_image = ship.image
		screen.blit(ship_image, (newpos))
		for particle in my_particles:
			particle.move()
			x = particle.x
			y = particle.y
			screen.blit(particle.image, (x,y))
			pygame.display.flip()
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_1:
					pygame.mouse.set_visible(False)
				elif event.key == pygame.K_2:
					pygame.mouse.set_visible(True)
	pygame.quit()
   
if __name__ == '__main__': main()