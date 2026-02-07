import pygame as pg
import sys

from visualization import Visualization
from walker_logic import Walker

width = 800
height = 800
tile_size = 10

total_walkers = 100
walkers = []

vis = Visualization(width, height, tile_size)

for _ in range(total_walkers):
    walker = Walker(vis.ROWS, vis.COLS)
    walkers.append(walker)

# main loop
running = True
clock = pg.time.Clock()

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    vis.draw()

    for walker in walkers:
        vis.draw_walker(walker)
        walker.step()
        if walker.touches_cluster(vis.grid):
            vis.grid[walker.row][walker.col] = 1
            walkers.remove(walker)
            walkers.append(Walker(vis.ROWS, vis.COLS))

    pg.display.flip()

    clock.tick(100)


pg.quit()
sys.exit()