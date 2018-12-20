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