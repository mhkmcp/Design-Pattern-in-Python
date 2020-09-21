import pygame
import time
#
# pygame.init()
# screen = pygame.display.set_mode((800, 600))
#
# pygame.draw.rect(screen, (255, 0, 34), pygame.Rect(42, 15, 40, 32))
# pygame.display.flip()
#
# time.sleep(20)

window_dimensions = 800, 600
screen = pygame.display.set_mode(window_dimensions)

players_quits = False

while not players_quits:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            players_quits = True

    pygame.display.flip()