"""
    Team: Eight minus one
    Description: A class for 'person agents' to be used in an abm within
                 Mesa.
"""

import mesa


EXIT1 = [(70, 18), (71, 18), (72, 18), (73, 18)]
EXIT2 = [(61, 33), (62, 33)]
EXIT3 = [(79, 158), (80, 158), (81, 158), (82, 158), (83, 158)]
EXIT4 = [(76, 181), (77, 181), (78, 181), (79, 181)]
ALL_EXITS = EXIT1 + EXIT2 + EXIT3 + EXIT4


class PersonAgent(mesa.Agent):
    def __init__(self, unique_id, model):
        # Initialize as Agent from mesa
        super().__init__(unique_id, model)

        # Define state etc. below
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
        if self.pos in EXIT1:
            self.model.grid.remove_agent(self)
            self.model.schedule.remove(self)
            self.model.person_agents -= 1
            self.model.counter_EXIT1 += 1
        elif self.pos in EXIT2:
            self.model.grid.remove_agent(self)
            self.model.schedule.remove(self)
            self.model.person_agents -= 1
            self.model.counter_EXIT2 += 1
        elif self.pos in EXIT3:
            self.model.grid.remove_agent(self)
            self.model.schedule.remove(self)
            self.model.person_agents -= 1
            self.model.counter_EXIT3 += 1
        elif self.pos in EXIT4:
            self.model.grid.remove_agent(self)
            self.model.schedule.remove(self)
            self.model.person_agents -= 1
            self.model.counter_EXIT4 += 1
        else:
            self.move()
