"""
    Team:
    Module description:
"""

import mesa
import numpy as np
from person_agent import PersonAgent
from wall_agent import WallAgent

# make a list of integer tuples from the wall_cood txt file, make sure to run
# blueprint_converter.py to get the correct wall_cood.txt file in your
# directory
with open('wall_cood2.txt') as f:
    mylist = [eval(i.strip()) for i in f]
WALLS = mylist

EMPTY = [(x, y) for x in range(10) for y in range(4)]


class EvacModel(mesa.Model):
    def __init__(self, N, width, height):
        self.num_agents = N
        # Default maximum visible distance
        self.max_vis = 5
        # Activate all agents in random order each step
        self.schedule = mesa.time.RandomActivation(self)
        self.grid = mesa.space.SingleGrid(width, height, False)

        # Initialize walls
        for pos in WALLS:
            w = WallAgent(self, pos)
            self.schedule.add(w)
            self.grid.position_agent(w, pos[0], pos[1])

        # Initialize persons in a loop
        for uid in range(self.num_agents):
            p = PersonAgent(uid, self)
            self.schedule.add(p)

            # Randomly place agent in grid
            r_id = np.random.randint(0, len(EMPTY))
            x, y = EMPTY.pop(r_id)
            self.grid.position_agent(p, x, y)

    def step(self):
        # Scheduler will execute every agent's step() method
        # schedule.agents !!!
        self.schedule.step()
