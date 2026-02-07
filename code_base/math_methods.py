import numpy as np

class Math_Logic:

    def calculate_distance(x1, y1, x2, y2):
        distance = np.sqrt(np.square(x2-x1) + np.square(y2-y1))

        return distance