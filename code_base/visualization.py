import pygame as pg
import numpy as np
import math as math

class Visualization:
    def __init__(self, width, height, tile_size):
        pg.init()

        self.zoom = 1.0
        self.min_zoom = .001
        self.max_zoom = 10.0

        self.dragging = False
        self.drag_start_mouse = (0, 0)
        self.drag_start_cam = (0,0)

        self.speed = 3
        
        self.top_left_col = 0.0 # Corner of grid space
        self.top_left_row = 0.0

        self.WIDTH = width
        self.HEIGHT = height
        self.TILE_SIZE = tile_size

        self.ROWS = self.HEIGHT // self.TILE_SIZE
        self.COLS = self.WIDTH // self.TILE_SIZE

        self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        pg.display.set_caption("DLA Simulation")

        self.BACKGROUND_COLOR = (20, 20, 20)

        self.grid = np.zeros((self.ROWS, self.COLS), dtype=int)
    
    def tile_position_after_zoom(self, row, col): # row and col are the looped over grid tiles in the draw function
        x = (col - self.top_left_col)*self.TILE_SIZE*self.zoom
        y = (row - self.top_left_row)*self.TILE_SIZE*self.zoom # new coordiante of top left grid tile after zoom
        size = self.TILE_SIZE * self.zoom
        return int(x), int(y), int(size)

    def calculate_color(self, row, col):
        # color should change is distance from seed increases
        center_row = self.ROWS//2
        center_col = self.COLS//2

        distance = ((row - center_row)**2 + (col - center_col)**2)**.5
        max_radius = min(self.ROWS, self.COLS) // 2

        # normalize distance
        t = min(distance / max_radius, 1)

        # shift from red to blue as radius increases
        r = int(255 * (1-t))
        g = 0
        b = int(255*t)

        return (r, g, b)

    def draw_cluster(self, cluster):
        
        for particle in cluster.particle_cords:
            col = particle[0]
            row = particle[1]

            color = cluster.color
            x, y, size = self.tile_position_after_zoom(row, col)

            if size <= 0:
                continue
            if x + size < 0 or y + size < 0:
                continue
            if x > self.WIDTH or y > self.HEIGHT:
                continue

            pg.draw.rect(
                self.screen,
                color,
                (x, y, size, size)
            )

    def draw_walker(self, walker):

        x, y, size = self.tile_position_after_zoom(walker.row, walker.col)

        pg.draw.rect(
            self.screen,
            (0, 255, 0),
            (x, y, size, size)
        )

    def draw_circle(self, center_x, center_y, radius, color):
        # Convert floats to ints
        center = (int(center_x), int(center_y))
        radius = int(radius)
        
        pg.draw.circle(
            self.screen, 
            color,       
            center,            
            radius,           
            1                  
        )


# rewrite the rendering to be O(num_particles) instead of O(grid)

# Write now, each frame I am asking the grid to give information on what tiles contain a particle
#  - This is wasted compute 
# Instead, for each cluster, store an array of particle positoins [(c_1, r_1), (c_2, r_2), ... (c_n, r_n)]
#  - Then, instead of looping over the entire grid and checking the tile value, loop over the individual cluster
#    arrays and draw the tiles from there
#  - IDEA: This way, if two clusters touch, then I can combine them into a single cluster maybe