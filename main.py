import pygame, math, sys, os
from Target import Target
from player import Player

class Game(object):
	def __init__(self):
		self.screen = pygame.display.set_mode((900,600))
		self.game_over = False
		self.clock = pygame.time.Clock()
		self.score = 0
		self.font = pygame.font.Font(None, 36)
		self.text = self.font.render("Score: {}".format(self.score),1,(0,0,255))
		self.textpos = self.text.get_rect()
		self.background = pygame.image.load("background.jpg").convert_alpha()
		self.backgroundRect = self.background.get_rect()
		self.textpos.topleft = self.background.get_rect().topright
		self.progress = 1
		self.targetsonscreen = 0
		self.targetlist = []
		self.player = Player()
	def update(self):
		pygame.event.get()
		self.text = self.font.render("Score: {}".format(self.score),1,(0,0,255))
		self.textpos = self.text.get_rect()
		self.textpos.topleft = self.background.get_rect().topright
		if self.targetsonscreen == 0:
			self.targetlist = [Target() for n in range(self.progress)]
			self.targetsonscreen = len(self.targetlist)
			self.progress += 1
		self.player.update()		
		for n in range(len(self.targetlist)):
			try:
				self.targetlist[n].update()
				if (self.targetlist[n].surf.get_width() + self.player.surf.get_width()) < (math.sqrt(math.pow(self.targetlist[n].rect.center[0] - self.player.rect.center[0],2) + pow(self.targetlist[n].rect.center[1] - self.player.rect.center[1],2))):
					self.game_over = True
				if self.targetlist[n].rect.left > 900 or self.targetlist[n].rect.right < 0 or self.targetlist[n].rect.top < 0 or self.targetlist[n].rect.bottom > 600:
					self.score += self.targetlist[n].size
					self.targetsonscreen -= 1
					self.targetlist.pop(n)
			except:
				print("no index")
	def draw(self):
		self.screen.blit(self.background, self.backgroundRect)
		self.screen.blit(self.text, self.textpos)
		for n in range (len(self.targetlist)):
			self.screen.blit(self.targetlist[n].surf,self.targetlist[n].rect)
		self.screen.blit(self.player.surf, self.player.rect)
		
pygame.init()
pygame.font.init()
g = Game()

while g.game_over is False:
	print pygame.mouse.get_pos()
	g.clock.tick(15)
	g.update()
	g.draw()
	pygame.display.flip()
#raw_input("Press Enter to continue...")
sys.exit()