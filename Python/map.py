import pygame 
from mapgen import map_gen
from tile import Tile
from player import Player
from camera import Camera

from random import randint
from pygame.locals import *

new_surface = pygame.Surface([480, 320])
end_surface = pygame.Surface([960, 640])
class Map:
	def __init__(self, width, height, tile, screen):
		self.width = width
		self.height = height
		self.tile = tile
		self.background = None
		
		#Calls our map generator to make an ascii map for us
		map = map_gen()
		
		#Looping through our 2d map array, it is oriented as a diamond
		for i in range(len(map)):
			if i < 30:
				even_x = 0
				even_y = i
				odd_x = 0
				odd_y = i - 1
			else: 
				even_x = i - int((len(map)/2))
				even_y = int(len(map)/2)
				odd_x = i - int((len(map)/2))
				odd_y = int(len(map)/2) - 1

			for j in range(len(map[i])):
				x_frame = randint(0,7)

				#Here is where we make choose what ascii character translates to tile
				if map[i][j] == '/':
						y_frame = 2
				elif map[i][j] == '&':
						y_frame = 1
				elif map[i][j] == '*':
						y_frame = 0

				if j%2 == 0:
					screen.blit(self.tile.file, ((even_x*self.tile.width),(even_y*self.tile.height)), 
						(x_frame*self.tile.width, y_frame*self.tile.height, self.tile.width, self.tile.height))
					even_x += 1
					even_y -= 1
				else:
					screen.blit(self.tile.file, ((odd_x*self.tile.width)+self.tile.width/2,(odd_y*self.tile.height) + self.tile.height/2), 
						(x_frame*self.tile.width, y_frame*self.tile.height, self.tile.width, self.tile.height))
					odd_x += 1
					odd_y -= 1

		pygame.image.save(screen, 'background.png')
		
	#Update splices a piece of our background to draw as our viewport/camera
	def update(self, screen, x_view, y_view):		
		s_width = 960						#WIDTH OF THE VIEWPORT
		s_height = 640						#HEIGHT OF THE VIEWPORT
		
		d_x = 0 							#X COORD TO DRAW VIEWPORT ON CANVAS
		d_y = 0								#Y COORD TO DRAW VIEWPORT ON CANVAS
		
		new_surface.blit(self.background, (d_x, d_y), (x_view, y_view, s_width/2, s_height/2))
		pygame.transform.scale2x(new_surface, end_surface)
		screen.blit(end_surface, (0, 0))