"""
    Team:
    Module description:
"""

import mesa
from evac_model import EvacModel


# Placeholder...
def agent_portrayal(agent):
    portrayal = {
        "Shape": "circle",
        "Filled": "true",
        "Layer": 0,
        "Color": "red",
        "r": 0.5,
    }
    return portrayal


grid = mesa.visualization.CanvasGrid(agent_portrayal, 10, 10, 500, 500)
server = mesa.visualization.ModularServer(
    EvacModel, [grid], "Evacuation Model", {"N": 10, "width": 10, "height": 10}
)
server.port = 8521  # The default
server.launch()
