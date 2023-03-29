import pygame


class Pipe():
	#def __init__(self):
		self.pipe = pygame.Rect(0,0, 0.15*screen_rect.width, 0.4*screen_rect.height)
		self.rect = self.pipe.get_rect()
		self.rect.topright = screen_rect.topright

		self.head = pygame.Rect(0, 0, 1.2*pipe.width, 0.1*pipe.height)
		self.rect = self.head.get_rect()
		self.rect.midbottom = screen_rect.midbottom
		pass
	
