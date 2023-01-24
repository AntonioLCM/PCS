"""
file name: blueprint_converter.py
project: Project Smoke
author: Abel John Oakley
"""

import mesa

class WallAgent(mesa.Agent):
    """
    class: create agents that represents walls inside the mesa simulation.
    A wall cannot be passable such that it contains the properties of a wall.
    """
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)


class EvacuationAgent(mesa.Agent):
    """
    class: create agents that evacuate a given building. 
    """

    def __init__(self, N):
        self.num_agents = N
        # Create agents
        for i in range(self.num_agents):
            a = MoneyAgent(i, self)