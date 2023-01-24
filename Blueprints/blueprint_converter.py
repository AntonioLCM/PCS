"""
file name: blueprint_converter.py
project: Project Smoke
author: Abel John Oakley
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
    #resize_image()
    #image_to_array()

main()