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

PERSON_S_E = [[(35, 12), (72, 29)],
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
            (s_x, s_y), end = PERSON_S_E[uid]
            p = PersonAgent(uid, self, (s_x, s_y), end)
            self.schedule.add(p)
            self.grid.position_agent(p, s_x, s_y)
        # p = PersonAgent(0, self, (35, 12), (72, 29))
        # q = PersonAgent(1, self, (34, 8), (72, 29))
        # z = PersonAgent(2, self, (137, 183), (80, 158))
        # w = PersonAgent(3, self, (93, 158), (77, 171))
        # a = PersonAgent(4, self, (15, 130), (77, 171))
        # x = PersonAgent(5, self, (13, 25), (62, 33))
        # i = PersonAgent(6, self, (44, 15), (72, 29))
        # j = PersonAgent(7, self, (106, 60), (72, 29))
        # o = PersonAgent(8, self, (132, 108), (80, 158))
        # g = PersonAgent(9, self, (91, 20), (72, 29))
        # c = PersonAgent(10, self, (144, 84), (62, 33))
        # b = PersonAgent(11, self, (139, 36), (62, 33))
        # y = PersonAgent(12, self, (44, 190), (80, 158))
        # k = PersonAgent(13, self, (56, 177), (77, 171))
        # v = PersonAgent(14, self, (10, 190), (80, 158))
        # u = PersonAgent(15, self, (13, 155), (77, 171))

        # d = PersonAgent(16, self, (16, 65), (72, 29))
        # h = PersonAgent(17, self, (118, 20), (72, 29))

        # self.schedule.add(p)
        # self.schedule.add(q)
        # self.schedule.add(z)
        # self.schedule.add(w)
        # self.schedule.add(a)
        # self.schedule.add(x)
        # self.schedule.add(i)
        # self.schedule.add(j)
        # self.schedule.add(o)
        # self.schedule.add(g)
        # self.schedule.add(c)
        # self.schedule.add(b)
        # self.schedule.add(y)
        # self.schedule.add(k)
        # self.schedule.add(v)
        # self.schedule.add(u)
        # self.schedule.add(d)
        # self.schedule.add(h)

        # print(uid, " ", x, y)

        # self.grid.position_agent(p, 35, 12)
        # self.grid.position_agent(q, 34, 8)
        # self.grid.position_agent(z, 137, 183)
        # self.grid.position_agent(w, 93, 158)
        # self.grid.position_agent(a, 15, 130)
        # self.grid.position_agent(x, 13, 25)
        # self.grid.position_agent(i, 44, 15)
        # self.grid.position_agent(j, 106, 60)
        # self.grid.position_agent(o, 132, 108)
        # self.grid.position_agent(g, 91, 20)
        # self.grid.position_agent(c, 144, 84)
        # self.grid.position_agent(b, 139, 36)
        # self.grid.position_agent(y, 44, 190)
        # self.grid.position_agent(k, 56, 177)
        # self.grid.position_agent(v, 10, 190)
        # self.grid.position_agent(u, 13, 155)
        # self.grid.position_agent(d, 16, 65)
        # self.grid.position_agent(h, 118, 20)

        # self.grid.position_agent(p, x, y)

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
