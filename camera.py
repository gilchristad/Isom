from rectangle import Rectangle

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
		