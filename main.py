import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 900, 900
TILES_SIZE = 4
ROWS = HEIGHT // TILES_SIZE
COLS = WIDTH // TILES_SIZE

# create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DLA Simulation")

BACKGROUND_COLOR = (20, 20, 20)
screen.fill(BACKGROUND_COLOR)

# main loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()
