"""
    Team: Eight minus one
    Description: A class for 'person agents' to be used in an abm within
                 Mesa.
"""

import mesa
from enum import IntEnum


EXITS = [(70, 27), (71, 27), (72, 27), (73, 27), (61, 34), (62, 34),
         (79, 156), (80, 156), (81, 156), (82, 156), (83, 156),
         (76, 171), (77, 171), (78, 171), (79, 171)]


# TODO: Something with these states.. maybe at some point
class State(IntEnum):
    HEALTHY = 0
    INJURED = 1


class PersonAgent(mesa.Agent):
    def __init__(self, unique_id, model):
        # Initialize as Agent from mesa
        super().__init__(unique_id, model)

        # Define state etc. below
        self.state = State.HEALTHY
        self.wall = False

    def _sees_exit(self):
        # Check if there is an exit in neighborhood with range max_vis (visible
        # distance in smoke). There's probably an efficient way to check this
        # instead of just checking all possible neighborhood cells
        pass

    def move(self):
        # Move to random empty neighboring cell
        neighbor_cells = self.model.grid.get_neighborhood(self.pos, moore=True)
        # This could probably be more efficient using numpy somehow..
        # TODO: ^
        possible_empty = [cell for cell in neighbor_cells
                          if self.model.grid.is_cell_empty(cell)]
        if len(possible_empty) != 0:
            self.model.grid.move_agent(self,
                                       self.random.choice(possible_empty))

    def step(self):
        if self.pos in EXITS:
            self.model.grid.remove_agent(self)
            self.model.schedule.remove(self)
        else:
            # Define step behavior
            self.move()
