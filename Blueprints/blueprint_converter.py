"""
file name: blueprint_converter.py
project: Project Smoke
author: Abel John Oakley
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def image_to_array(image='Resized Blueprints/blueprint1_resized.png'):
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

    plt.imshow(img_array)                               # check input with plot
    plt.show()

    return img_array


def resize_image(image='Original Blueprints/blueprint1.png'):
    """
    function: this function takes a given image and required width
    and resizes it with respect to the required width.
    input: img, basewidth
    return: resized_image
    """
    basewidth = 200
    img = Image.open(image)                                     # open image    
    wpercent = (basewidth/float(img.size[0]))                    
    hsize = int((float(img.size[1]) * float(wpercent)))         
    resized_image = img.resize((basewidth, hsize),              
                                Image.BICUBIC)

    # save image
    resized_image.save('Resized Blueprints/blueprint1_resized.png')  

    return resized_image


def get_wall_locations(save=1):
    """
    function: this function takes an binary array of an image and converts
    it to a list of coordinates [(x1,y1), (xn,yn)] of the location of the wall.
    input: img_array, save
    return: list_wall
    """
    img_array = image_to_array()
    list_wall = []
    for n, x in enumerate(img_array):                   # loop through array
        for m, y in enumerate(x):                       # and find all cood
            if y > 0:                                   # where a wall segment
                list_wall.append((n, m))                # is found

    if save == 1:                                       # save coordinates
        with open("wall_cood.txt", 'w') as f:           # to save file
            for line in list_wall:                      # wall_cood.txt
                f.write(f"{line}\n")

    # print(list_wall)
    return list_wall


get_wall_locations()
# resize_image()

# check program
# image_to_array()
