import pygame
from random import randint

pygame.init()
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption('Flappy Bird')
running = True
GREEN = (0, 200, 0)
RED = (255,0,0)
BLACK = (0,0,0)
clock = pygame.time.Clock()
background = GREEN

font = pygame.font.SysFont('sans', 30)
text = font.render("Random", True, BLACK)

while running:		
	clock.tick(60)
	screen.fill(background)

	mouse_x, mouse_y = pygame.mouse.get_pos()	

	pygame.draw.rect(screen,RED,(50,50,150,50))
	screen.blit(text, (50,50))

	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				if (mouse_x>50) and (mouse_x<200) and (mouse_y>50) and (mouse_y<100):
					background = (randint(0,255),randint(0,255),randint(0,255))
					print("Right click on red rectangle")

		if event.type == pygame.QUIT:
			running = False
				
	pygame.display.flip()

pygame.quit()
