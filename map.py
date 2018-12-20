import pygame
from pygame.locals import * 

from player import Player
from rectangle import Rectangle
from tile import Tile
from camera import Camera

from random import randint

#Holds our total map
class Map:
	def __init__(self, width, height, tile, screen):
		self.width = width
		self.height = height
		self.tile = tile
		self.background = None
		
		#We initially draw the tiles here to inevitably save as a png, then use as a background
		for i in range(59):
			if (i%2) == 0:
				for j in range(30):
					x_rand = randint(0, 7)
					y_rand = randint(0, 2)
					screen.blit(self.tile.file, ((j*64),(i*16)), (x_rand*64, y_rand*32, 64, 32))
			else:
				for j in range(29):
					x_rand = randint(0, 7)
					y_rand = randint(0, 2)
					screen.blit(self.tile.file, ((j*64)+32,(i*16)), (x_rand*64, y_rand*32, 64, 32))
		
		pygame.image.save(screen, 'background.png')
		
	#This is currently drawing our scrolling viewport
	def update(self, screen, x_view, y_view):		
		s_width = 960						#WIDTH OF THE VIEWPORT
		s_height = 640						#HEIGHT OF THE VIEWPORT
		
		if self.width - x_view < s_width:
			s_width = self.width - s_x
			
		if self.height - y_view < s_height:
			s_height = self.height - s_y
		
		d_x = 0 							#X COORD TO DRAW VIEWPORT ON CANVAS
		d_y = 0								#Y COORD TO DRAW VIEWPORT ON CANVAS
		
		screen.blit(self.background, (d_x, d_y), (x_view, y_view, s_width, s_height))
