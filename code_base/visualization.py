import pygame as pg
import numpy as np
import random as rand

class Visualization:
    def __init__(self, width, height, tile_size):
        pg.init()

        self.WIDTH = width
        self.HEIGHT = height
        self.TILE_SIZE = tile_size

        self.ROWS = self.HEIGHT // self.TILE_SIZE
        self.COLS = self.WIDTH // self.TILE_SIZE

        self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        pg.display.set_caption("DLA Simulation")

        self.BACKGROUND_COLOR = (20, 20, 20)

        self.grid = np.zeros((self.ROWS, self.COLS), dtype=int)
        self.grid[self.ROWS//2, self.COLS//2] = 1 # put a 1 in the central tile to be the seed

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

    def draw(self):
        self.screen.fill(self.BACKGROUND_COLOR)

        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.grid[row, col] == 1:

                    color = self.calculate_color(row, col)

                    pg.draw.rect(
                        self.screen,
                        color,
                        (col * self.TILE_SIZE, row * self.TILE_SIZE, self.TILE_SIZE, self.TILE_SIZE)
                    )

    def draw_walker(self, walker):
        pg.draw.rect(
            self.screen,
            (0, 255, 0),
            (walker.col * self.TILE_SIZE, walker.row * self.TILE_SIZE, self.TILE_SIZE, self.TILE_SIZE)
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


