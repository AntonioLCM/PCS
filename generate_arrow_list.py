"""
file name: arrow_placement.py
project: Project Smoke
author: Abel John Oakley
"""

import Blueprints.arrow_priority as arp
from arrow_class import Arrow


"""
arrow       = (x, y, direction, distance)
x,y         = coordinates of the arrow
direction   =   0: north
                1: east
                2: south
                3: west
distance    = distance towards the exit
"""
arrow_list = [(33, 47, 2), (32, 70, 3), (32, 94, 0),
              (74, 120, 1), (80, 120, 3), (168, 128, 0),
              (168, 102, 0), (168, 95, 2), (168, 78, 1),
              (126, 32, 3), (102, 22, 3), (90, 22, 1),
              (56, 33, 3), (46, 33, 1)]


def generate_arrow_list(exits):
    """

    """
    arrows = []
    for (x, y, d) in arrow_list:
        arrows.append(Arrow((x, y), d, arp.exit_priority((x, y), exits)))
    return arrows
