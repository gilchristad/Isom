#Our tiles can be loaded with different sprites
class Tile(object):
	def __init__(self, image_file, width, height):
		self.file = image_file
		self.width = width
		self.height = height