"""
    Team: Eight minus one
    Description: The (agent based) model definition for an evacuation
                 simulation using Mesa.
"""

import mesa
from mesa.datacollection import DataCollector
import numpy as np
from person_agent import PersonAgent
from wall_agent import WallAgent

# make a list of integer tuples from the wall_cood txt file, make sure to run
# blueprint_converter.py to get the correct wall_cood.txt file in your
# directory
with open('Blueprints/wall_cood.txt') as f:
    mylist = [eval(i.strip()) for i in f]
WALLS = mylist

# Find all empty spaces within building. (building is smaller than image grid)
# TODO: remove inaccesible SPACES from EMPTY as well.. There should be
#       a better way than finding the coordinates and hardcoding them..
#       probably
EMPTY = list(set([(x, y) for x in range(4, 147) for y in range(4, 196)])
             - set(WALLS))


class EvacModel(mesa.Model):
    def __init__(self, N, width, height):
        self.person_agents = N
        # Default maximum visible distance
        self.max_vis = 5
        # Activate all agents in random order each step
        self.schedule = mesa.time.RandomActivation(self)
        self.grid = mesa.space.SingleGrid(width, height, False)
        self.datacollector = DataCollector(model_reporters={
                                           "agent_count": lambda m: m.person_agents})

        # Initialize walls
        for pos in WALLS:
            w = WallAgent(self, pos)
            self.schedule.add(w)
            self.grid.position_agent(w, pos[0], pos[1])

        # Initialize persons in a loop
        # Random placement on empty cell within 'building'
        for uid in range(self.person_agents):
            p = PersonAgent(uid, self)
            self.schedule.add(p)

            # Randomly place agent in grid
            r_id = np.random.randint(0, len(EMPTY))
            x, y = EMPTY.pop(r_id)
            self.grid.position_agent(p, x, y)

    def step(self):
        # Scheduler will execute every agent's step() method
        # schedule.agents !!!
        self.datacollector.collect(self)
        self.schedule.step()
