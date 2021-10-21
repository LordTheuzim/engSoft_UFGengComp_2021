import sys
import pygame
		
def run_game():
	pygame.init()
	screen = pygame.display.set_mode((1100,700))
	pygame.display.set_caption("Alien Invasion")
	
	while True:
# Watch for keyboard and mouse events.
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
					sys.exit()
# Make the most recently drawn screen visible.
			pygame.display.flip()
# Make a game instance, and run the game.

run_game()
