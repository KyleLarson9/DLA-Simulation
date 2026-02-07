import random as rand
import numpy as np

class Walker:
    def __init__(self, rows, cols, center_row, center_col, cluster_radius, kill_radius):

        # spawn walkers between kill radius and cluster radius

        self.ROWS = rows
        self.COLS = cols
        
        theta = rand.uniform(0, 2*np.pi)  # random angle in radians
        r = (kill_radius + cluster_radius)/2 

        self.row = int(center_row + r * np.sin(theta))
        self.col = int(center_col + r * np.cos(theta))

        # clamp to grid bounds
        self.row = max(0, min(self.ROWS - 1, self.row))
        self.col = max(0, min(self.COLS - 1, self.col))

    def step(self):

        # Chose a random direction (up, down, left, right)
        delta_row, delta_col = rand.choice([
            (-1, 0), (1, 0), (0, -1), (0, 1)
        ])

        # check that the move stays in bounds 

        new_row = self.row + delta_row
        new_col = self.col + delta_col

        # clamp to bounds
        if 0 <= new_row < self.ROWS:
            self.row = new_row

        if 0 <= new_col < self.COLS:
            self.col = new_col

    def exceeds_kill_radius(self, center_row, center_col, kill_radius):
        distance = ((self.row - center_row)**2 + (self.col - center_col)**2)**0.5
        return distance > kill_radius

    def touches_cluster(self, grid):
        # check value of tile around walker to see if it is part of the cluster

        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i == j == 0:
                    continue

                # check if this position is part of the cluster
                r = self.row + i
                c = self.col + j

                if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                    if grid[r][c] == 1:
                        return True
                
        return False






        
    