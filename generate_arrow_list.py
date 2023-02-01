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
# arrow_list = [(33, 47, 2), (32, 70, 3), (32, 94, 0),
#               (74, 120, 1), (80, 120, 3), (168, 128, 0),
#               (168, 102, 0), (168, 95, 2), (168, 78, 1),
#               (126, 32, 3), (102, 22, 3), (90, 22, 1),
#               (56, 33, 3), (46, 33, 1)]

arrow_list = [(32,32,2), (32,71,3), (32,128,0),
              (167,31,2), (168,128,0), (168,78,1),
              (97,21,3), (102,21,1), (101,119,1),
              (98,119,3), (82,31,3), (127,31,1),
              (57,126,3), (140,128,1), (148,30,1),
              (31,109,0), (75,120,3), (131,120,1),
              (169,103,0), (168,55,2)]


def generate_arrow_list(exits):
    """

    """
    arrows = []
    for (x, y, d) in arrow_list:
        arrows.append(Arrow((x, y), d, arp.exit_priority((x, y), exits)))
    return arrows
