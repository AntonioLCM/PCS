"""
file    : resize_image.py
team    : Team 8-1
project : PCS
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def resize_image(image='Blueprints/Original Blueprints/blueprint1_remade.png',
                 resampling=1,
                 basewidth=200):
    """
    function: this function takes a given image and required width
    and resizes it with respect to the required width.
    input: img, basewidth
    return: resized_image
    """

    img = Image.open(image)                               # open image
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    if resampling == 0:                                   # resampling nearest
        resized_image = img.resize((basewidth, hsize),
                                   Image.NEAREST)

    if resampling == 1:                                   # resampling bicubic
        resized_image = img.resize((basewidth, hsize),
                                   Image.BICUBIC)

    if resampling == 2:                                   # resampling lanczos
        resized_image = img.resize((basewidth, hsize),
                                   Image.LANCZOS)

    # save image
    resized_image.save('Blueprints/Resized Blueprints/blueprint1_resized.png')

    return resized_image
