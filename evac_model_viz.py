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


grid = mesa.visualization.CanvasGrid(agent_portrayal, 100, 100, 700, 700)
server = mesa.visualization.ModularServer(
    EvacModel, [grid], "Evacuation Model", {"N": 100, "width": 100, "height": 100}
)
server.port = 8521  # The default
server.launch()
