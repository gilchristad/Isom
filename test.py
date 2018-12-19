import pygame
import map

from pygame.locals import *

white = (255, 255, 255)
pygame.init()

#Right now the way setup works is that it initially creates a largers window @ 1920x960 
#When the Map is initialized it populates the screen space with our tiles
#We then use pygame's ability to save a screen cap of said screen space
#We store that screen cap as our larger map's background
#From there we are drawing a spliced image from the background 
#----------------------------------------------------------------------
#|                                                                    |
#|                                                                    |
#|             viewport                                               |
#|      ------------------------------                                |
#|      |                            |                                |
#|      |                            |                                |
#|      |                            |                                |
#|      |                            |                                |
#|      |                            |                                |
#|      |                            |                                |
#|      |                            |                                |
#|      |                            |                                |
#|      |                            |                                |
#|      |                            |                                |
#|      ------------------------------                                |
#|                                                                    |
#|                                                                    |
#|                                                                    |
#|                                                                    |
#|                                                                    |
#----------------------------------------------------------------------

#There may be a more ideal solution to this problem.  One thing to note it order for us to use different tiles,
#during the population phase we need to create a trivial 2d array using simple ascii characters which will differentiate the tiles
#//////////////////////////////
#/****************************/
#******************************				/ = null
#/********&&&&&&&&&&**********/				& = grass
#/********&&&&&&&&&&**********/				* = water etc
#/********&&&&&&&&&&**********/
#******************************
#/****************************/
#//////////////////////////////



screen = pygame.display.set_mode([1920,960])
pygame.display.set_caption('Isometric Testing')
clock = pygame.time.Clock()
screen.fill(white)

#Pulling in the sprites and sprite sheets
isom_small_tile = pygame.image.load('Tiles/32x16/sample.png')
isom_medium_tile = pygame.image.load('Tiles/64x32/sample.png')
player_sample = pygame.image.load('Player/playerSheet.png')

new_tile = map.Tile(isom_medium_tile)
new_map = map.Map(1920, 960, new_tile, screen)

new_player = map.Player(23, 32, player_sample)

screen = pygame.display.set_mode([960, 640])

new_map.background = pygame.image.load('background.png')

camera = map.Camera(0, 0, 960, 640, 1920, 960)
camera.follow(new_player, 480, 320)

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