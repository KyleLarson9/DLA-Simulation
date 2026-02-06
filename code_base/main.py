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

    walker.step()

    pg.display.flip()

    clock.tick(10000)


pg.quit()
sys.exit()