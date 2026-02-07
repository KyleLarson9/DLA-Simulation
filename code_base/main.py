import pygame as pg
import sys

from visualization import Visualization
from walker_logic import Walker
from math_methods import Math_Logic
from zoom_logic import Zoom_Logic

width = 800
height = 800
tile_size = 1

total_walkers = 1000
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

        if event.type == pg.MOUSEWHEEL:
            mouse_x, mouse_y = pg.mouse.get_pos() # in pixels
            Zoom_Logic.zoom(mouse_x, mouse_y, vis, event)
                   
        # start dragging
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            vis.dragging = True
            vis.drag_start_mouse = pg.mouse.get_pos()
            vis.drag_start_cam = (vis.top_left_col, vis.top_left_row)

        # stop dragging
        if event.type == pg.MOUSEBUTTONUP and event.button == 1:
            vis.dragging = False

        if vis.dragging:
            Zoom_Logic.drag_camera(vis, *pg.mouse.get_pos())

        keys = pg.key.get_pressed()

        if keys[pg.K_r]:
            vis.zoom = 1
            vis.top_left_col = 0
            vis.top_left_row = 0

        print(vis.zoom)
        if vis.zoom <= 1:
            vis.zoom = 1
            vis.top_left_col = 0
            vis.top_left_row = 0

        Zoom_Logic.pan(keys, vis)

    vis.draw()

    for walker in walkers[:]:
        # vis.draw_walker(walker)
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


