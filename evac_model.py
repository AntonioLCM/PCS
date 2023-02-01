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
from arrow_location import *
from viz_arrow_agent import *

# make a list of integer tuples from the wall_cood txt file, make sure to run
# blueprint_converter.py to get the correct wall_cood.txt file in your
# directory
with open('Blueprints/wall_cood.txt') as f:
    mylist = [eval(i.strip()) for i in f]
    
WALLS = mylist
WALLS = [(y,151-x) for (x,y) in WALLS]
arrows = arrow_config(arrow_list_type=1)
ARROWS = [(x,151-y) for (x,y,z) in arrows]

# Find all empty spaces within building. (building is smaller than image grid)
# TODO: remove inaccesible SPACES from EMPTY as well.. There should be
#       a better way than finding the coordinates and hardcoding them..
#       probably
EMPTY = list(set([(x, y) for x in range(4, 196) for y in range(4, 147)])
             - set(WALLS))


class EvacModel(mesa.Model):
    def __init__(self, N, width, height):
        self.person_agents = N
        self.counter_EXIT1 = 0
        self.counter_EXIT2 = 0
        self.counter_EXIT3 = 0
        self.counter_EXIT4 = 0
        # Default maximum visible distance
        self.max_vis = 100
        # Activate all agents in random order each step
        self.schedule = mesa.time.RandomActivation(self)
        self.grid = mesa.space.SingleGrid(width, height, False)
        self.datacollector = DataCollector(model_reporters={
                                           "Exit1": lambda m: m.counter_EXIT1, "Exit2": lambda m: m.counter_EXIT2, "Exit3": lambda m: m.counter_EXIT3, "Exit4": lambda m: m.counter_EXIT4})

        # Initialize walls
        for pos in WALLS:
            w = WallAgent(self, pos)
            self.schedule.add(w)
            self.grid.position_agent(w, pos[0], pos[1])
        
        # Code to visualize arrow
        # for pos in ARROWS:
        #     a = viz_arrow_agent(self,pos)
        #     self.schedule.add(a)
        #     self.grid.position_agent(a,pos[0], pos[1])


        # Initialize persons in a loop
        # Random placement on empty cell within 'building'
        # for uid in range(self.person_agents):
        #     p = PersonAgent(uid, self)
        #     self.schedule.add(p)

        #     # Randomly place agent in grid
        #     r_id = np.random.randint(0, len(EMPTY))
        #     x, y = EMPTY.pop(r_id)
        #     self.grid.position_agent(p, x, y)
            # self.grid.position_agent(p, 33, 46)

    def step(self):
        # Scheduler will execute every agent's step() method
        # schedule.agents !!!
        self.datacollector.collect(self)
        self.schedule.step()
        
    def run_model(self, steps):
        # Because the model has no inherent end conditions,
        # the user must specify how many steps to run it for.
        for i in range(steps):
            self.step()
            
