import random as rand

class Walker:
    def __init__(self, rows, cols):

        self.ROWS = rows
        self.COLS = cols

        edge = rand.choice([1, 2, 3, 4])

        if edge == 1:
            self.row = 0
            self.col = rand.randint(0, cols -1)
        elif edge == 2:
            self.row = rows - 1
            self.col = rand.randint(0, cols - 1)
        elif edge == 3:
            self.row = rand.randint(0, rows - 1)
            self.col = 0
        else:
            self.row = rand.randint(0, rows - 1)
            self.col = cols - 1

        self.COLOR = (0, 255, 0)   
        
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






        
    
