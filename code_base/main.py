import pygame as pg
import sys

from visualization import Visualization
from walker_logic import Walker

vis = Visualization()
walker = Walker(vis.ROWS, vis.COLS)

# main loop
running = True
clock = pg.time.Clock()

# vis.calc_rand_tiles()

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    vis.draw()
    vis.draw_walker(walker)

    pg.display.flip()

    clock.tick(10)


pg.quit()
sys.exit()

# import pygame
# import sys
# import random
# import math

# # Initialize pygame
# pygame.init()

# # Window size
# WIDTH, HEIGHT = 800, 800
# TILE_SIZE = 4
# ROWS = HEIGHT // TILE_SIZE
# COLS = WIDTH // TILE_SIZE

# # Create the window
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Fractal DLA Simulation: Red to Blue")

# # Colors
# BACKGROUND_COLOR = (20, 20, 20)  # dark background
# screen.fill(BACKGROUND_COLOR)

# # DLA cluster grid
# grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

# # Seed particle in the center
# center_row, center_col = ROWS//2, COLS // 2
# grid[center_row][center_col] = 1

# # Function to compute distance from center
# def distance_from_center(row, col):
#     return math.hypot(row - center_row, col - center_col)

# # Map distance to red→blue gradient
# def color_from_distance(row, col, max_distance):
#     dist = distance_from_center(row, col)
#     ratio = dist / max_distance  # 0 = center, 1 = corner
#     r = max(0, int(255 * (1 - ratio)))  # red decreases
#     g = 0
#     b = min(255, int(255 * ratio))      # blue increases
#     return (r, g, b)

# # Draw seed particle
# pygame.draw.rect(screen, (255, 0, 0),
#                  (center_col * TILE_SIZE, center_row * TILE_SIZE, TILE_SIZE, TILE_SIZE))
# pygame.display.flip()

# # Function to spawn a walker at a random edge
# def spawn_walker():
#     edge = random.choice(['top', 'bottom', 'left', 'right'])
#     if edge == 'top':
#         return [0, random.randint(0, COLS-1)]
#     elif edge == 'bottom':
#         return [ROWS-1, random.randint(0, COLS-1)]
#     elif edge == 'left':
#         return [random.randint(0, ROWS-1), 0]
#     else:  # right
#         return [random.randint(0, ROWS-1), COLS-1]

# # Function to check if a cell touches the cluster
# def is_adjacent_to_cluster(row, col):
#     for dr in [-1, 0, 1]:
#         for dc in [-1, 0, 1]:
#             r, c = row + dr, col + dc
#             if 0 <= r < ROWS and 0 <= c < COLS:
#                 if grid[r][c] == 1:
#                     return True
#     return False

# # Maximum possible distance from center (corner)
# max_distance = math.hypot(center_row, center_col)

# # Main loop
# running = True
# clock = pygame.time.Clock()

# walkers = [spawn_walker() for _ in range(50)]  # multiple walkers for speed

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     new_walkers = []
#     for walker in walkers:
#         row, col = walker

#         # Random walk (8 directions)
#         dr = random.choice([-1, 0, 1])
#         dc = random.choice([-1, 0, 1])
#         if 0 <= row + dr < ROWS:
#             row += dr
#         if 0 <= col + dc < COLS:
#             col += dc

#         # Check if walker touches cluster
#         if is_adjacent_to_cluster(row, col):
#             grid[row][col] = 1
#             color = color_from_distance(row, col, max_distance)
#             pygame.draw.rect(screen, color,
#                              (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))
#             pygame.display.update()
#             new_walkers.append(spawn_walker())  # spawn a new walker
#         else:
#             new_walkers.append([row, col])  # keep walking

#     walkers = new_walkers
#     clock.tick(20000)

# pygame.quit()
# sys.exit()
