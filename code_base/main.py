import pygame as pg
import sys

from visualization import Visualization

vis = Visualization()

# main loop
running = True
clock = pg.time.Clock()

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    vis.draw()
    clock.tick(60)


pg.quit()
sys.exit()
