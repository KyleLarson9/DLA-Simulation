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
        # self.row = rand.randint(0, rows - 1)
        # self.col = rand.randint(0, cols - 1)


        self.COLOR = (0, 255, 0)   

    