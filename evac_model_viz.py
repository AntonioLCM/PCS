"""
    Team: Eight minus one
    Description: Initializes a webserver and uses JavaScript to visualize
                 the evacuation model.
"""

import mesa
from evac_model import EvacModel
from wall_agent import WallAgent
from person_agent import PersonAgent


NUM_AGENTS = 18


# Define what the agents should look like in the visualization dependent
# on their type.
def agent_portrayal(agent):
    portrayal = {
        "Filled": "true",
        "Layer": 0,
        "Color": "red",
    }

    if isinstance(agent, WallAgent):
        portrayal["Color"] = "black"
        portrayal["Shape"] = "rect"
        portrayal["w"] = 1
        portrayal["h"] = 1

    if isinstance(agent, PersonAgent):
        portrayal["Shape"] = "circle"
        portrayal["r"] = 2

    return portrayal


# Gridsize 151 x 200, on 800 x 800 canvas
grid = mesa.visualization.CanvasGrid(agent_portrayal, 151, 200, 800, 800)

chart = mesa.visualization.ChartModule([{"Label": "Exit1", "Color": "Black"},
                                        {"Label": "Exit2", "Color": "red"},
                                        {"Label": "Exit3", "Color": "green"},
                                        {"Label": "Exit4", "Color": "yellow"}],
                                       data_collector_name='datacollector')
server = mesa.visualization.ModularServer(
    EvacModel, [grid, chart], "Evacuation Model", {"N": NUM_AGENTS,
                                                   "width": 151,
                                                   "height": 200}
)
server.port = 8521
server.launch()
