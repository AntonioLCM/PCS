"""
file name: resize_image.py
project: Project Smoke
author: Abel John Oakley
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def resize_image(image='Original Blueprints/blueprint1.png'):
    """
    function: this function takes a given image and required width
    and resizes it with respect to the required width.
    input: img, basewidth
    return: resized_image
    """
    basewidth = 300
    img = Image.open(image)                                     # open image    
    wpercent = (basewidth/float(img.size[0]))                    
    hsize = int((float(img.size[1]) * float(wpercent)))         
    resized_image = img.resize((basewidth, hsize),              
                                Image.BICUBIC)

    # save image
    resized_image.save('Resized Blueprints/blueprint1_resized.png')  

    return resized_image