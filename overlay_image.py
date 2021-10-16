# import the necessary packages
from __future__ import print_function
import numpy as np
import argparse
import cv2
import PIL
from PIL import Image
from PIL import ImageChops # used for multiplying images

ap = argparse.ArgumentParser()
ap.add_argument("-b", "--background", type=str, required=True,
                help="background image")
ap.add_argument("-o", "--overlay", type=str, required=True,
                help="image to overlay")
ap.add_argument("-n", "--name", type=str, required=True,
                help="name of the image to output")
args = vars(ap.parse_args())
# open images
background = Image.open(args["background"])
foreground     = Image.open(args["overlay"])

background.paste(foreground, (0, 0), foreground)
background.save(args["name"])
# python overlay_image.py -b 1.png -o trans.png -n test.png