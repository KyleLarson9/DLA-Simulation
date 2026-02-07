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

    def draw(self):
        self.screen.fill(self.BACKGROUND_COLOR)

        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.grid[row, col] == 1:
                    pg.draw.rect(
                        self.screen,
                        (255, 0, 0),
                        (col * self.TILE_SIZE, row * self.TILE_SIZE, self.TILE_SIZE, self.TILE_SIZE)
                    )

    def draw_walker(self, walker):
        pg.draw.rect(
            self.screen,
            (0, 255, 0),
            (walker.col * self.TILE_SIZE, walker.row * self.TILE_SIZE, self.TILE_SIZE, self.TILE_SIZE)
        )

    def draw_R_max(self, center_x, center_y, max_r, max_c):
        # radius of the cluster

        # each time a particle is added to the cluster calcualte its distance
        #  - if that distance is greater than the current longest distance, update that distance
        #    and that will be the radius of the cluster

        temp = 1

    def draw_R_kill(self):
        # radius of kill zone (if walker goes past it gets eliminated to save cpu space)
        temp = 1

    def calculate_color(self):
        # color should change is distance from seed increases
        color = 1

