"""
    Team:
    Module description:
"""

import mesa
from person_agent import PersonAgent


class EvacModel(mesa.Model):
    def __init__(self, N, width, height):
        self.num_agents = N
        # Activate all agents in random order each step
        self.schedule = mesa.time.RandomActivation(self)
        self.grid = mesa.space.SingleGrid(width, height, False)

        # Initialize agents in a loop probably
        for uid in range(self.num_agents):
            a = PersonAgent(uid, self)
            self.schedule.add(a)

            # Place agent in grid
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))

    def step(self):
        # Scheduler will execute every agent's step() method
        self.schedule.step()
