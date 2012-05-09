import pygame
from math import cosin, sin, pi, sqrt, pow
from random import random, uniform

class Player(object):
	def __init__(self):
		self.surf = pygame.transform.smoothscale(pygame.image.load("player.png").convert_alpha(), (30,30))
		self.rect = self.image.get_rect()
	def update(self):
		self.cursor = pygame.mouse.get_pos()
		self.rect.center = (cursor[0], cursor[1])
		if self.rect.bottom > 600:
			self.rect.bottom = 600
		if self.rect.right > 900:
			self.rect.right = 900
			
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
		self.surf = pygame.transform.smoothscale(self.surf, (2.71828*self.size, 2.71828*self.size))
		
class Game(object):
	def __init__(self):
		self.screen = pygame.display.set_mode((900,600))
		self.game_over = False
		self.clock = pygame.time.Clock()
		self.score = 0
		self.font = pygame.font.Font(None, 36)
		self.text = self.font.render("Score: {}".format(self.score),1,(0,0,255))
		self.textpos = self.text.get_rect()
		self.background = pygame.image.load("background.png").convert_alpha()
		self.backgroundRect = self.background.get_rect()
		self.textpos.topleft = self.background.get_rect().topright
		self.progress = 1
		self.targetsonscreen = 0
		self.targetlist = []
		self.player = Player()
	def update(self):
		self.text = self.font.render("Score: {}".format(self.score),1,(0,0,255))
		self.textpos = self.text.get_rect()
		self.textpos.topleft = self.background.get_rect().topright
		if self.targetsonscreen == 0:
			self.targetlist = [Target() for n in range(self.progress)]
			self.progress += 1
		self.player.update()
		for n in range(len(self.targetlist)):
			try:
				self.targetlist[n].update()
				if (self.targetlist[n].surf.get_width() + self.player.surf.get_width()) < (math.sqrt(math.pow(self.targetlist[n].rect.center[0] - self.player.rect.center[0],2) + pow(self.targetlist[n].rect.center[1] - self.player.rect.center[1],2))):
					self.game_over = True
				if self.targetlist[n].rect.left > 900 or self.targetlist[n].rect.right < 0 or self.targetlist[n].rect.top < 0 or self.targetlist[n].rect.bottom > 600:
					self.score += self.targetlist[n].size
					self.targetlist.pop(n)
			except:
				print("no index")
	def draw(self):
		self.screen.blit(self.background, self.backgroundrect)
		self.screen.blit(self.text, self.textpos)
		for n in range (len(self.targetlist)):
			self.screen.blit(self.targetlist[n].surf,self.targetlist[n].rect)
		self.screen.blit(self.player.surf, self.player.rect)
		
pygame.init()
pygame.font.init()
g = Game()

while g.game_over is false:
	g.update()
sys.exit()