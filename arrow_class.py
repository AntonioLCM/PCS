"""
    Team: Eight minus one
    Description: A class for 'arrows' to be used in an abm within
                 Mesa.
"""

class Arrow:
    def __init__(self, pos, dir, exit_priority):
        self.pos = None
        self.dir = None
        self.exit_priority = None