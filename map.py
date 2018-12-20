import pygame 
from mapgen import map_gen
from random import randint
from pygame.locals import *

class Rectangle:
	def __init__(self, left, top, width, height):
		self.left = left or 0
		self.top = top or 0
		self.width = width or 0
		self.height = height or 0
		self.right = self.left + self.width
		self.bottom = self.top + self.height
		
	def set(self, left, top):
		self.left = left
		self.top = top
		self.right = (self.left + self.width)
		self.bottom = (self.top + self.height)
		
	def within(self, r):
		return (r.left <= self.left and r.right >= self.right and r.top <= self.top and r.bottom >= self.bottom)
				
#Holds our total map
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
		
#Our tiles can be loaded with different sprites
class Tile(object):
	def __init__(self, image_file):
		self.file = image_file
	
class Player:
	def __init__(self, width, height, file):
		self.width = width
		self.height = height
		self.file = file
		self.x = 50
		self.y = 50
		self.x_velocity = 0
		self.y_velocity = 0
		self.friction = 0.9
		self.frames = 8
		self.ticks = 20
		self.tick_count = 0
		self.x_frame = 0
		self.y_frame = 0
		
	def draw_player(self, screen, x_view, y_view):
		screen.blit(self.file, (((self.x - self.width/2) - x_view), ((self.y - self.height/2) - y_view)), (self.x_frame*self.width, self.y_frame*self.height, self.width, self.height))
		
	def update_direction(self):
		if self.x_velocity == 0 and self.y_velocity == 0:
			self.y_frame = 0
		elif self.x_velocity > 0:
			self.y_frame = 2
		elif self.x_velocity < 0:
			self.y_frame = 3 
			
	def update(self, keys, screen, x_view, y_view):
		
		#updating hitbox of the player as they are moving
		self.hit_box = Rectangle(self.x, self.y, self.width, self.height)
		
		#upper bounds for our velocity
		if self.x_velocity > 10:
			self.x_velocity = 10
		if self.y_velocity > 10:
			self.y_velocity = 10
		if self.y_velocity < -10:
			self.y_velocity = -10
		if self.x_velocity < -10:
			self.x_velocity = -10
			
		#Increments the velocities when the keys are pressed
		if keys[K_w] and not keys[K_a] and not keys[K_d]:
			self.y_velocity -= 1
		elif keys[K_a] and not keys[K_w] and not keys[K_s]:
			self.x_velocity -= 1
		elif keys[K_s] and not keys[K_a] and not keys[K_d]:
			self.y_velocity += 1
		elif keys[K_d] and not keys[K_w] and not keys[K_s]:
			self.x_velocity += 1
		
		#Diagonal slope
		if keys[K_w] and keys[K_a]:
			self.x_velocity -= 1
			self.y_velocity -= 0.5
		elif keys[K_w] and keys[K_d]:
			self.x_velocity += 1
			self.y_velocity -= 0.5
		elif keys[K_s] and keys[K_a]:
			self.x_velocity -= 1
			self.y_velocity += 0.5
		elif keys[K_s] and keys[K_d]:
			self.x_velocity += 1
			self.y_velocity += 0.5
			
		#Incrementing the velocities based on friction
		self.x_velocity *= self.friction
		self.y_velocity *= self.friction
		
		#Actually updating the current players place on the map
		self.x = int(self.x_velocity) + int(self.x)
		self.y = int(self.y_velocity) + int(self.y)
		
		#Once the velocity has slowed down due to the friction we bring out character back to standing still
		if (self.x_velocity > -0.2 and self.x_velocity < 0) or (self.x_velocity > 0 and self.x_velocity < 0.2):
			self.x_velocity = 0
			
		if (self.y_velocity > -0.2 and self.y_velocity < 0) or (self.y_velocity > 0 and self.y_velocity < 0.2):
			self.y_velocity = 0
			
		#looping through the x_frames from our sprite sheet
		self.tick_count += 1
		if(self.tick_count >= self.ticks):
			self.tick_count = 0
			if self.x_frame < self.frames - 1:
				self.x_frame += 1
			else:
				self.x_frame = 0
			
		#bounds 
		if self.x <= 30:
			self.x = 30
		elif self.x >= 1890:
			self.x = 1890
		if self.y <= 18:
			self.y = 18
		elif self.y >= 930:
			self.y = 930
			
		#As it says updates the direction the sprite should be facing	
		self.update_direction()
		
		#We always update the player on the screen
		self.draw_player(screen, x_view, y_view)
		
#Moving our camera goal to follow player
class Camera:
	def __init__(self, x_view, y_view, screen_width, screen_height, map_width, map_height):
		self.x_view = x_view or 0
		self.y_view = y_view or 0
		self.w_view = screen_width
		self.h_view = screen_height
		self.x_dead_zone = 0
		self.y_dead_zone = 0
		self.followed = None
		self.viewport = Rectangle(self.x_view, self.y_view, screen_width, screen_height)
		self.map = Rectangle(0, 0, map_width, map_height)
		
	#Designates the target in which the viewport will use as reference
	def follow(self, player, x_dead_zone, y_dead_zone):
		self.followed = player
		self.x_dead_zone = x_dead_zone
		self.y_dead_zone = y_dead_zone
		
	def update(self):
		#If logic blocks set up to increment the cameras x and y values.  As the player moves to the sides, or up and down
		#the appropriate increments to the x and y values happen.  Right now the camera isn't incrementing at the rate the player is moving
		#A work around to this might need to have the player at the center of the camera when not in range of the deadzones (ie at the edges)
		if self.followed:
			if self.followed.x - self.x_view + self.x_dead_zone > self.w_view:
				self.x_view = self.followed.x - (self.w_view - self.x_dead_zone)
			elif self.followed.x - self.x_dead_zone < self.x_view:
				self.x_view = self.followed.x - self.x_dead_zone
			
			if self.followed.y - self.y_view + self.y_dead_zone > self.h_view:
				self.y_view = self.followed.y - (self.h_view - self.y_dead_zone)
			elif self.followed.y - self.y_dead_zone < self.y_view:
				self.y_view = self.followed.y - self.y_dead_zone
				
		#Our viewport is a rectangle so the hit box needs to be updated constantly
		self.viewport.set(self.x_view, self.y_view)
		
		#This checks bounds on the the current position of the viewport and stops increments to the x and y values of the viewport
		if not self.viewport.within(self.map):
			if self.viewport.left < self.map.left:
				self.x_view = self.map.left
			if self.viewport.top < self.map.top:
				self.y_view = self.map.top
			if self.viewport.right > self.map.right:
				self.x_view = self.map.right - self.w_view
			if self.viewport.bottom > self.map.bottom:
				self.y_view = self.map.bottom - self.h_view
		