"""
file    : blueprint_converter.py
team    : Team 8-1
project : PCS
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from Blueprints.get_wall_locations import get_wall_locations
from Blueprints.image_to_array import image_to_array
from Blueprints.resize_image import resize_image


def main():
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
    resize_image()
    img_array = image_to_array()
    get_wall_locations(img_array)


main()
