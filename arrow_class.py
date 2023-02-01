"""
    Team: Eight minus one
    Description: A class for 'arrows' to be used in an abm within
                 Mesa.
"""

import numpy as np


class Arrow:

    def __init__(self, pos, direction, exit_priority):
        self.pos = pos
        self.dir = direction
        self.exit_priority = exit_priority

    def is_in_range(self, loc, dist):
        x, y = loc
        a, b = self.pos
        return np.floor(np.sqrt(np.square(x - a)
                                + np.square(y - b))) <= dist
