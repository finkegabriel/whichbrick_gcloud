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


# # load the image
# image = cv2.imread(args["background"])
# img2_overlay = args["overlay"]
# img2_output = ""
# img3_overlay = ""

# def convertImage(image):
#     img = Image.open(image)
#     img = img.convert("RGBA")
  
#     datas = img.getdata()
  
#     newData = []
  
#     for items in datas:
#         if items[0] == 255 and items[1] == 255 and items[2] == 255:
#             newData.append((255, 255, 255, 0))
#         else:
#             newData.append(items)
#     return np.array(newData)

# imgs = convertImage(img2_overlay)

# # loop over the alpha transparency values
# for alpha in np.arange(0, 1.1, 0.1)[::-1]:
# 	# create two copies of the original image -- one for
# 	# the overlay and one for the final output image
# 	# overlay = image.copy()
# 	# output = img2_overlay.copy()
# 	img3_overlay = imgs
# 	img2_output = np.array(img2_overlay)
# 	print(img3_overlay)
# 	print("-----------")
# 	print(img2_output)
# 	# draw a red rectangle surrounding Adrian in the image
# 	# along with the text "PyImageSearch" at the top-left
# 	# corner
# 	# cv2.rectangle(img3_overlay, (420, 205), (595, 385),
# 	# 	(0, 0, 255), -1)
# 	# cv2.putText(img3_overlay, "PyImageSearch: alpha={}".format(alpha),
# 	# 	(10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 3)

# 	# apply the overlay
# 	cv2.addWeighted(img3_overlay, alpha, img2_output, 1 - alpha,
# 		0, img2_output)
# # show the output image
# 	print("alpha={}, beta={}".format(alpha, 1 - alpha))
# 	cv2.imwrite(args["name"], img3_overlay)

# 	# cv2.waitKey(0)


# open images
background = Image.open(args["background"])
foreground     = Image.open(args["overlay"])

# def convertImage():
#     img = Image.open(args["overlay"])
#     img = img.convert("RGBA")
  
#     datas = img.getdata()
  
#     newData = []
  
#     for items in datas:
#         if items[0] == 255 and items[1] == 255 and items[2] == 255:
#             newData.append((255, 255, 255, 0))
#         else:
#             newData.append(items)
  
#     img.putdata(newData)
#     img.save("trans.png", "PNG")
#     print("Successful")
  
# convertImage()


background.paste(foreground, (0, 0), foreground)
background.save(args["name"])
# python overlay_image.py -b 1.png -o trans.png -n test.png