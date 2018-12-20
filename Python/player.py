import pygame
from pygame.locals import * 

from rectangle import Rectangle

new_surface = pygame.Surface([23, 32], pygame.SRCALPHA)
end_surface = pygame.Surface([46, 64], pygame.SRCALPHA)
black = (0, 0, 0, 0)

class Player:
	def __init__(self, width, height, file):
		self.width = width
		self.height = height
		self.file = file
		self.x = 50
		self.y = 50
		self.x_velocity = 0
		self.y_velocity = 0
		self.friction = 0.8
		self.frames = 8
		self.ticks = 20
		self.tick_count = 0
		self.x_frame = 0
		self.y_frame = 0
		
	#Quick scaling trick to make things seem 2x as big will become a nightmare for rendering
	def draw_player(self, screen, x_view, y_view):
		new_surface.fill((0, 0, 0, 0))
		new_surface.blit(self.file, (0, 0), (self.x_frame*self.width, self.y_frame*self.height, self.width, self.height))
		pygame.transform.scale2x(new_surface, end_surface)
		screen.blit(end_surface, (((self.x - self.width/2) - x_view), ((self.y - self.height/2) - y_view)))
		
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
			self.y_velocity -= 0.6666666
		elif keys[K_w] and keys[K_d]:
			self.x_velocity += 1
			self.y_velocity -= 0.6666666
		elif keys[K_s] and keys[K_a]:
			self.x_velocity -= 1
			self.y_velocity += 0.6666666
		elif keys[K_s] and keys[K_d]:
			self.x_velocity += 1
			self.y_velocity += 0.666666
			
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
		elif self.x >= 2340:
			self.x = 2340
		if self.y <= 18:
			self.y = 18
		elif self.y >= 1220:
			self.y = 1220
			
		#Updates the direction the sprite should be facing	
		self.update_direction()
		
		#We always update the player on the screen
		self.draw_player(screen, x_view, y_view)