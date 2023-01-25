"""
    Team: Eight minus one
    Description: A class for 'wall agents' to be used in an abm within
                 Mesa. Walls can't do much.
"""

import mesa


class WallAgent(mesa.Agent):
    def __init__(self, model, pos):
        # Initialize as Agent from mesa
        super().__init__(pos, model)

        # Define state etc. below
        self.wall = True
        self.pos = pos

    def move(self):
        pass

    def step(self):
        # Define step behavior
        self.move()
