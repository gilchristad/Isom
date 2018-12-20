import sys
sys.path.insert(0, 'Python')

import pygame
import map
import mapgen

from pygame.locals import *

white = (255, 255, 255)
map_width = 1920
map_height = 960
screen_width = 960
screen_height = 640

#Initializing pygame and the first screen interation
pygame.init()
screen = pygame.Surface([map_width, map_height])
pygame.display.set_caption('Isometric Testing')
clock = pygame.time.Clock()

#Pulling in the sprites and sprite sheets
isom_small_tile = pygame.image.load('Tiles/32x16/sample.png')
isom_medium_tile = pygame.image.load('Tiles/64x32/Tile-Sheet.png')
player_sample = pygame.image.load('Player/playerSheet.png')

#Creating the objects which are required currently in the game
new_tile = map.Tile(isom_medium_tile, 64, 32)
new_map = map.Map(map_width, map_height, new_tile, screen)
new_player = map.Player(23, 32, player_sample)

screen = pygame.display.set_mode([screen_width, screen_height])

#Pulling the background image that was generated by our mapgen
new_map.background = pygame.image.load('background.png')

#Creating our camera/viewport that will follow the player
camera = map.Camera(0, 0, screen_width, screen_height, map_width, map_height)
camera.follow(new_player, screen_width/2, screen_height/2)

def main():
	start = True
	
	while start:
		screen.fill(white)
		keys=pygame.key.get_pressed()
		new_map.update(screen, camera.x_view, camera.y_view)
		new_player.update(keys, screen, camera.x_view, camera.y_view)
		camera.update()


		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
		
		pygame.display.update()
		clock.tick(90)
		
main()