"""
    Team: Eight minus one
    Description: A class for 'arrows' to be used in an abm within
                 Mesa.
"""


class Arrow:

    def __init__(self, pos, direction, exit_priority):
        self.pos = pos
        self.dir = direction
        self.exit_priority = exit_priority

    def _is_in_range(self, dist):
        pass
