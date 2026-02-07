import numpy as np

class Math_Logic:

    def calculate_distance(x1, y1, x2, y2):
        distance = ((x2-x1)**2 + (y2-y1)**2)**.5

        return distance