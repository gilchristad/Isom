import pygame 
from mapgen import map_gen
from random import randint
from pygame.locals import *

class Map:
	def __init__(self, width, height, tile, screen):
		self.width = width
		self.height = height
		self.tile = tile
		self.background = None
		
		#Calls our map generator to make an ascii map for us
		map = map_gen()

		print("Printing length of row 29!")
		print(len(map[29]))
		
		for i in range(len(map)):
			if i < 30:
				x_counter = 0
				y_counter = i
				for j in range(len(map[i])):
					x_index = randint(0, 7)
					
					if map[i][j] == '/':
						y_index = 2
					elif map[i][j] == '&':
						y_index = 1
					elif map[i][j] == '*':
						y_index = 0
						
					if j%2 == 0:
						screen.blit(self.tile.file, ((x_counter*64),(y_counter*32)), (x_index*64, y_index*32, 64, 32))
						x_counter += 1
						y_counter -= 1
			else:
				x_counter = i - int((len(map)/2))
				y_counter = int(len(map)/2)
				
				for j in range(len(map[i])):
					x_index = randint(0, 7)
						
					if map[i][j] == '/':
						y_index = 2
					elif map[i][j] == '&':
						y_index = 1
					elif map[i][j] == '*':
						y_index = 0
							
					if j%2 == 0:
						screen.blit(self.tile.file, ((x_counter*64),(y_counter*32)), (x_index*64, y_index*32, 64, 32))
						x_counter += 1
						y_counter -= 1
						
		for i in range(len(map)):
			if i < 30:
				x_counter = 0
				y_counter = i - 1
				for j in range(len(map[i])):
					x_index = randint(0, 7)
					
					if map[i][j] == '/':
						y_index = 2
					elif map[i][j] == '&':
						y_index = 1
					elif map[i][j] == '*':
						y_index = 0
						
					if j%2 == 1:
						screen.blit(self.tile.file, ((x_counter*64)+32,(y_counter*32) + 16), (x_index*64, y_index*32, 64, 32))
						x_counter += 1
						y_counter -= 1
						
			else:
				x_counter = i - int((len(map)/2))
				y_counter = int(len(map)/2) - 1
				
				for j in range(len(map[i])):
					x_index = randint(0, 7)
						
					if map[i][j] == '/':
						y_index = 2
					elif map[i][j] == '&':
						y_index = 1
					elif map[i][j] == '*':
						y_index = 0
							
					if j%2 == 1:
						screen.blit(self.tile.file, ((x_counter*64)+32,(y_counter*32)+ 16), (x_index*64, y_index*32, 64, 32))
						x_counter += 1
						y_counter -= 1
					
							
				#else:
				#	screen.blit(self.tile.file, ((j*32),(i*16) + 16), (0*64, 0*32, 64, 32))
				
		#for i in range(59):
		#	if (i%2) == 0:
		#		for j in range(30):
		#			x_rand = randint(0, 7)
		#			y_rand = randint(0, 2)
		#			screen.blit(self.tile.file, ((j*64),(i*16)), (x_rand*64, y_rand*32, 64, 32))
		#	else:
		#		for j in range(29):
		#			x_rand = randint(0, 7)
		#			y_rand = randint(0, 2)
		#			screen.blit(self.tile.file, ((j*64)+32,(i*16)), (x_rand*64, y_rand*32, 64, 32))
		
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