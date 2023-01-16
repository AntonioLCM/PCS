"""
    Team:
    Module description:
"""

import mesa
from person_agent import PersonAgent


class EvacModel(mesa.Model):
    def __init__(self, N, width, height):
        self.num_agents = N
        # Default maximum visible distance
        self.max_vis = 5
        # Activate all agents in random order each step
        self.schedule = mesa.time.RandomActivation(self)
        self.grid = mesa.space.SingleGrid(width, height, False)

        # Initialize agents in a loop probably
        for uid in range(self.num_agents):
            p = PersonAgent(uid, self)
            self.schedule.add(p)

            # Randomly place agent in grid
            self.grid.position_agent(p, 'random')

    def step(self):
        # Scheduler will execute every agent's step() method
        # schedule.agents !!!
        self.schedule.step()
