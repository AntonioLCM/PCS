"""
file name: arrow_priority.py
project: Project Smoke
author: Abel John Oakley
"""

import numpy as np


def arrow_priority(exit_priority):
    """
    function: this function takes a list with as first element
    the location of an arrow in tuple form, and as second element
    the closest exit. It then calculates the distance between
    the two. 
    input: exit_priority [(n,m), (x, y)]
    output: (x,y,distance)
    """
    [(x,y), (n,m)] = exit_priority                      
    
    distance = abs(x - n) + abs(y - m)                  # manhatten distance

    return (x,y,distance)

def exit_priority(arrow, exits):
    """
    function: this function calculates the manhatten distance
    between an arrow and multiple exits to find and couple
    the closest exit to an given arrow.
    input: arrow (n,m), exits [(x1,y1), (x2,y2)]
    return: exit_priority [(n,m), (x, y)]
    """
    dis = 10000                                         # set large distance
    for x,y in exits:                                   # loop through possible exits
        n,m = arrow
        new_dis = abs(x - n) + abs(y - m)               # find manhatten distance
        if new_dis < dis:                               # check shortest distance
            dis = new_dis
            exit_priority = [(n,m), (x,y)]              # save both arrow and exit

    return exit_priority
