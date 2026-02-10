import pygame as pg
import sys
import random as rand

from visualization import Visualization
from walker_logic import Walker
from cluster_logic import Cluster
from math_methods import Math_Logic
from zoom_logic import Zoom_Logic

width = 800
height = 800
tile_size = 2

walkers_per_cluster = 500

total_clusters = 2
clusters = []

radii_difference = 30

vis = Visualization(width, height, tile_size)

center_row = vis.ROWS // 2 
center_col = vis.COLS // 2

for _ in range(total_clusters):

    x = rand.randint(0, vis.ROWS - 1)
    y = rand.randint(0, vis.COLS - 1)

    r = rand.randint(0, 255)
    g = rand.randint(0, 255)
    b = rand.randint(0, 255)
    color = (r, g, b)

    # x = vis.COLS // 2
    # y = vis.ROWS // 2
    cluster_radius = 0
    kill_radius = cluster_radius + radii_difference

    cluster = Cluster(x, y, vis.ROWS, vis.COLS, walkers_per_cluster, cluster_radius, kill_radius, vis.grid, color)
    clusters.append(cluster)

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

        if vis.zoom <= 1:
            vis.zoom = 1
            vis.top_left_col = 0
            vis.top_left_row = 0

        Zoom_Logic.pan(keys, vis)
    
    for cluster in clusters:
        # vis.draw_circle(cluster.col, cluster.row, cluster.kill_radius, (100, 100, 100))

        vis.draw_cluster(cluster)
       
        for walker in cluster.walkers[:]:
                # vis.draw_walker(walker)
                walker.step()

                if walker.exceeds_kill_radius(cluster.row, cluster.col, cluster.kill_radius):
                    cluster.walkers.remove(walker)
                    cluster.walkers.append(Walker(vis.ROWS, vis.COLS, cluster.row, cluster.col, cluster.cluster_radius, cluster.kill_radius))
                    continue

                if walker.touches_cluster(vis.grid):

                    # add to coordiantes to cluster position array
                    cluster.add_particle(walker)
                    vis.grid[walker.row][walker.col] = 1
                    cluster.walkers.remove(walker)

                    radius = Math_Logic.calculate_distance(cluster.row, cluster.col, walker.row, walker.col)

                    if radius > cluster.cluster_radius:
                        cluster.cluster_radius = radius
                        cluster.kill_radius = cluster.cluster_radius + radii_difference
                    
                    cluster.walkers.append(Walker(vis.ROWS, vis.COLS, cluster.row, cluster.col, cluster.cluster_radius, cluster.kill_radius))

                    continue


    pg.display.flip()

    clock.tick(60)  # limit to 60 FPS

    print(f"FPS: {clock.get_fps():.2f}")  # prints current FPS


pg.quit()
sys.exit()


# later try to make it so that if two clusters meet, they combine
#   - Find the center of the cluster
#   - And recalculate the kill and cluster radii and combine their walkers