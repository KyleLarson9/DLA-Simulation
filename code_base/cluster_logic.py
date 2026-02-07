from walker_logic import Walker

class Cluster:
    def __init__(self, start_row, start_col, grid_rows, grid_cols, total_walkers, cluster_radius, kill_radius, grid):
        self.row = start_row
        self.col = start_col
        self.grid = grid  # reference to the shared grid
        self.kill_radius = kill_radius
        self.cluster_radius = cluster_radius

        # mark the seed
        self.grid[self.row, self.col] = 1

        # spawn walkers around cluster
        self.walkers = []
        for _ in range(total_walkers):
            walker = Walker(grid_rows, grid_cols, self.row, self.col, cluster_radius, kill_radius)
            self.walkers.append(walker)
            # print(self.walkers)