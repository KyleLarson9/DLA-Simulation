import pygame as pg
import sys

from visualization import Visualization
from walker_logic import Walker
from math_methods import Math_Logic

width = 800
height = 800
tile_size = 1

total_walkers = 1500
walkers = []

cluster_radius = 0
radii_difference = 30
kill_radius = cluster_radius + radii_difference # in grid units

vis = Visualization(width, height, tile_size)

center_row = vis.ROWS // 2 
center_col = vis.COLS // 2

for _ in range(total_walkers):
    walker = Walker(vis.ROWS, vis.COLS, center_row, center_col, cluster_radius, kill_radius)
    walkers.append(walker)

# main loop
running = True
clock = pg.time.Clock()

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    vis.draw()

    for walker in walkers[:]:
        vis.draw_walker(walker)
        walker.step()

        if walker.exceeds_kill_radius(center_row, center_col, kill_radius):
            walkers.remove(walker)
            walkers.append(Walker(vis.ROWS, vis.COLS, center_row, center_col, cluster_radius, kill_radius))
            continue

        if walker.touches_cluster(vis.grid):
            vis.grid[walker.row][walker.col] = 1
            walkers.remove(walker)

            radius = Math_Logic.calculate_distance(center_row, center_col, walker.row, walker.col)

            if radius > cluster_radius:
                cluster_radius = radius
                kill_radius = cluster_radius + radii_difference
                print(cluster_radius)
            
            walkers.append(Walker(vis.ROWS, vis.COLS, center_row, center_col, cluster_radius, kill_radius))

            continue
        
    # vis.draw_circle(
    #             center_x=center_col * vis.TILE_SIZE + vis.TILE_SIZE//2,
    #             center_y=center_row * vis.TILE_SIZE + vis.TILE_SIZE//2,
    #             radius=cluster_radius * vis.TILE_SIZE,
    #             color = (0, 0, 255)
    #         )
        
    # vis.draw_circle(
    #             center_x=center_col * vis.TILE_SIZE + vis.TILE_SIZE//2,
    #             center_y=center_row * vis.TILE_SIZE + vis.TILE_SIZE//2,
    #             radius=kill_radius * vis.TILE_SIZE,
    #             color = (255, 0, 0)
    #         )


    pg.display.flip()

    clock.tick(60)


pg.quit()
sys.exit()


