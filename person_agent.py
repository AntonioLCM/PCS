"""
    Team:
    Module description:
"""

import mesa


class PersonAgent(mesa.Agent):
    def __init__(self, unique_id, model):
        # Initialize as Agent from mesa
        super().__init__(unique_id, model)

        # Define state etc. below

    def move(self):
        # Define person movement
        # (self.model.grid.move_agent(self, new_position)
        pass

    def step(self):
        # Define step behavior
        self.move()
        pass
