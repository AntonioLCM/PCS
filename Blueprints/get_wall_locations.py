"""
file    : get_wall_locations.py
team    : Team 8-1
project : PCS
"""


def get_wall_locations(img_array, save=1):
    """
    function: this function takes an binary array of an image and converts
    it to a list of coordinates [(x1,y1), (xn,yn)] of the location of the wall.
    input: img_array, save
    return: list_wall
    """

    list_wall = []
    for n, x in enumerate(img_array):                   # loop through array
        for m, y in enumerate(x):                       # and find all cood
            if y > 0:                                   # where a wall segment
                list_wall.append((n, m))                # is found

    if save == 1:                                       # save coordinates
        with open("Blueprints/wall_cood.txt", 'w') as f:           # to save file
            for line in list_wall:                      # wall_cood.txt
                f.write(f"{line}\n")
    return list_wall
