import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 800
TILE_SIZE = 4
ROWS = HEIGHT // TILE_SIZE
COLS = WIDTH // TILE_SIZE

# create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DLA Simulation")

BACKGROUND_COLOR = (20, 20, 20)
screen.fill(BACKGROUND_COLOR)

grid_matrix = [[0 for _ in range(COLS)] for _ in range(ROWS)]
grid_matrix[ROWS//2][COLS//2] = 1

def draw_grid(screen, grid, tile_size):
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == 1:
                pygame.draw.rect(
                    screen,
                    (255, 0, 0),
                    (col * tile_size, row * tile_size, tile_size, tile_size)
                )

# main loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)

    draw_grid(screen, grid_matrix, TILE_SIZE)

    pygame.display.flip()

pygame.quit()
sys.exit()
