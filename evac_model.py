"""
    Team: Eight minus one
    Description: The (agent based) model definition for an evacuation
                 simulation using Mesa.
"""

import mesa
from mesa.datacollection import DataCollector
from person_agent import PersonAgent
from wall_agent import WallAgent

# Make a list of integer tuples from the wall_cood txt file, make sure to run
# blueprint_converter.py to get the correct wall_cood.txt file in the
# Blueprints directory
with open('Blueprints/wall_cood.txt') as f:
    wall_list = [eval(i.strip()) for i in f]
WALLS = wall_list

NUM_WALLS = len(WALLS)

# Find all empty spaces within building. (building is smaller than image grid)
EMPTY = list(set([(x, y) for x in range(4, 147) for y in range(4, 196)])
             - set(WALLS))

# Improved arrow config
PERSON_SE_IMPROVED = [[(35, 12), (72, 29)],
                      [(34, 8), (72, 29)],
                      [(137, 183), (80, 158)],
                      [(93, 158), (77, 171)],
                      [(15, 130), (77, 171)],
                      [(13, 25), (62, 33)],
                      [(44, 15), (72, 29)],
                      [(106, 60), (72, 29)],
                      [(132, 108), (80, 158)],
                      [(91, 20), (72, 29)],
                      [(144, 84), (62, 33)],
                      [(139, 36), (62, 33)],
                      [(44, 190), (80, 158)],
                      [(56, 177), (77, 171)],
                      [(10, 190), (80, 158)],
                      [(13, 155), (77, 171)],
                      [(16, 65), (72, 29)],
                      [(118, 20), (72, 29)]]


# Original arrow config
PERSON_SE_ORIGINAL = [[(35, 12), (72, 29)],
                      [(34, 8), (72, 29)],
                      [(137, 183), (80, 158)],
                      [(93, 158), (77, 171)],
                      [(15, 130), (62, 33)],
                      [(13, 25), (62, 33)],
                      [(44, 15), (72, 29)],
                      [(106, 60), (77, 171)],
                      [(132, 108), (72, 29)],
                      [(91, 20), (72, 29)],
                      [(144, 84), (62, 33)],
                      [(139, 36), (62, 33)],
                      [(44, 190), (80, 158)],
                      [(56, 177), (77, 171)],
                      [(10, 190), (80, 158)],
                      [(13, 155), (62, 33)],
                      [(16, 65), (72, 29)],
                      [(118, 20), (72, 29)]]


class EvacModel(mesa.Model):
    def __init__(self, N, width, height):
        self.person_agents = N
        self.counter_EXIT1 = 0
        self.counter_EXIT2 = 0
        self.counter_EXIT3 = 0
        self.counter_EXIT4 = 0

        # Activate all agents in random order each step
        self.schedule = mesa.time.RandomActivation(self)
        self.grid = mesa.space.SingleGrid(width, height, False)
        self.datacollector = DataCollector(model_reporters={
                                           "agentCount": lambda m: m.schedule.get_agent_count() - (NUM_WALLS + 1),
                                           "Exit1": lambda m: m.counter_EXIT1,
                                           "Exit2": lambda m: m.counter_EXIT2,
                                           "Exit3": lambda m: m.counter_EXIT3,
                                           "Exit4": lambda m: m.counter_EXIT4})

        # Initialize walls
        for pos in WALLS:
            w = WallAgent(self, pos)
            self.schedule.add(w)
            self.grid.position_agent(w, pos[0], pos[1])

        # Initialize persons in a loop
        for uid in range(self.person_agents):
            (s_x, s_y), end = PERSON_SE_IMPROVED[uid]
            p = PersonAgent(uid, self, (s_x, s_y), end)
            self.schedule.add(p)
            self.grid.position_agent(p, s_x, s_y)

    def step(self):
        # Scheduler will execute every agent's step() method
        self.datacollector.collect(self)
        self.schedule.step()

    def run_model(self, steps):
        # Because the model has no inherent end conditions,
        # the user must specify how many steps to run it for.
        for i in range(steps):
            self.step()
