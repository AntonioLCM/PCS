"""
file name: image_to_array.py
project: Project Smoke
author: Abel John Oakley
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def image_to_array(image='Blueprints/Resized Blueprints/blueprint1_resized.png'):
    """
    function: this function transforms a given blueprint (image) with walls
    and returns an array with the locations of every wall (empty = 0, wall = 1)
    and the shape of the image
    input: img
    returns: img_array, (x,y)
    """

    img = Image.open(image).convert('L')                # open image
    img_array = np.array(img)                           # convert to array
    img_array = ~img_array                              # invert image
    img_array[img_array > 0] = 1
    # img_shape = np.shape(img_array)                   # give image shape

    img_list = img_array.tolist()
    
    plt.imshow(img_array)                               # check input with plot
    plt.show()
    return img_list

