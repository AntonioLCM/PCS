"""
file    : blueprint_converter.py
team    : Team 8-1
project : PCS
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from get_wall_locations import *
from image_to_array import *
from resize_image import *


def main():
    img_array = image_to_array()
    get_wall_locations(img_array)

    """
    function: resize_image
    parameters: resampling, basewidth

    resampling:
    resize takes resampling parameter with three resampling methods
    NEAREST - resampling = 0
    BICUBIC - resampling = 1
    LANCZOS - resampling = 2
    default = 1

    basewidth:
    basewidth takes an integer to scale image to
    default = 200
    """

    #resize_image()
    #image_to_array()

    # resize_image()
    # image_to_array()


main()
