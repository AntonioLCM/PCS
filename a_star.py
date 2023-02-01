
from Blueprints.image_to_array import *
import numpy as np

class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)


def main():
    #poppetje1 = [(94,133), (18,71)]
    #poppetje2 = [(106,140), (18,71)]
    #poppetje3 = [(79,98), (18,71)]
    #poppetje4 = [(164,139), (181,77)]
    #poppetje5 = [(157,63), (181,77)]
    #poppetje6 = [(187,105), (181,77)]
    #poppetje7 = [(57,140), (181,77)]
    #poppetje8 = [(58,105), (181,77)]
    #poppetje9 = [(70,105), (181,77)]
    #poppetje10 = [(14,92), (18,71)]
    #poppetje11 = [(44,83), (18,71)]
    #poppetje12 = [(94,37), (181,77)]
    #poppetje13 = [(128,16), (18,71)]
    #poppetje14 = [(36,16), (181,77)]
    #poppetje15 = [(68,17), (18,71)]
    #poppetje16 = [(188,16), (18,71)]
    #poppetje17 = [(70,45), (18,71)]

    grid = image_to_array()

    #start = (70, 18)
    #end = (30, 40)

    path1 = astar(grid, (38,15), (181,78))

    path2 = astar(grid, (130,17), (18,71))
    print(path1)
    print(path2)

if __name__ == '__main__':
    main()