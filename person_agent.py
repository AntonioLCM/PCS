"""
    Team: Eight minus one
    Description: A class for 'person agents' to be used in an abm within
                 Mesa.
"""

import mesa
import a_star as pf


EXIT1 = [(70, 29), (71, 29), (72, 29), (73, 29)]
EXIT2 = [(61, 33), (62, 33)]
EXIT3 = [(79, 158), (80, 158), (81, 158), (82, 158), (83, 158)]
EXIT4 = [(76, 171), (77, 171), (78, 171), (79, 171)]
ALL_EXITS = EXIT1 + EXIT2 + EXIT3 + EXIT4


class PersonAgent(mesa.Agent):
    def __init__(self, unique_id, model, pos, end):
        # Initialize as Agent from mesa
        super().__init__(unique_id, model)

        # Define state etc. below
        self.pos = pos
        self.end = end
        # Calculate path from self.pos to self.end using the A* algorithm
        self.path = pf.main(list(self.pos), list(self.end))

    def move(self):
        # If no arrows in visibility range randomwalk, if arrow(s) then find
        # best exit according to distance between arrow and exit and move
        # towards this exit. After passing the arrow keep moving in direction
        # of arrow.
        next_loc = self.path.pop(0)
        self.model.grid.move_agent(self, next_loc)

    def step(self):
        if self.pos in ALL_EXITS:
            if self.pos in EXIT1:
                self.model.counter_EXIT1 += 1
            elif self.pos in EXIT2:
                self.model.counter_EXIT2 += 1
            elif self.pos in EXIT3:
                self.model.counter_EXIT3 += 1
            elif self.pos in EXIT4:
                self.model.counter_EXIT4 += 1
            self.model.grid.remove_agent(self)
            self.model.schedule.remove(self)
            self.model.person_agents -= 1
        else:
            self.move()
