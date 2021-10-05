# import the necessary packages
from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2
from skimage import filters
import csv
import math
import os

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="path to the input image")
ap.add_argument("-l", "--label", required=True,
                help="image label")
ap.add_argument("-w", "--width", type=float, required=True,
                help="width of the left-most object in the image (in inches)")
ap.add_argument("-s", "--scale", type=str, required=True,
                help="scale of the yaml file")
args = vars(ap.parse_args())

# load the image, convert it to grayscale, and blur it slightly
image = cv2.imread(args["image"])
# print("pippipppp ",image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# gray = cv2.GaussianBlur(gray, (7, 7), 0)
# perform edge detection, then perform a dilation + erosion to
# close gaps in between object edges
edged = cv2.Canny(gray, 50, 100)
edged = cv2.dilate(edged, None, iterations=1)
edged = cv2.erode(edged, None, iterations=1)
# find contours in the edge map
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
                        cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
# sort the contours from left-to-right and initialize the
# 'pixels per metric' calibration variable
(cnts, _) = contours.sort_contours(cnts)
pixelsPerMetric = None

for c in cnts:
	# if the contour is not sufficiently large, ignore it
	if cv2.contourArea(c) < 100:
		continue
	# compute the rotated bounding box of the contour
	orig = image.copy()
	box = cv2.minAreaRect(c)
	box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
	box = np.array(box, dtype="int")
	# order the points in the contour such that they appear
	# in top-left, top-right, bottom-right, and bottom-left
	# order, then draw the outline of the rotated bounding
	# box
	box = perspective.order_points(box)
	## Uncomment if you want bounding boi's around your img
	# cv2.drawContours(orig, [box.astype("int")], -1, (0, 255, 0), 1)
	# # loop over the original points and draw them
	# for (x, y) in box:
	# 	cv2.circle(orig, (int(x), int(y)), 5, (0, 0, 255), -1)

def height_width_image(tl,tr,br,bl):
	width = math.sqrt(((tl[0]-tr[0])**2)+((tr[1]-tl[1])**2))
	height = math.sqrt(((bl[0]-br[0])**2)+((br[1]-bl[1])**2))
	print(width,height)
	return width,height

def center(tl,tr,br,bl):
	xcenter = ((tl[0]+br[0])/2) 
	ycenter = ((tl[1]+br[1])/2)
	return xcenter,ycenter

# unpack the ordered bounding box, then compute the midpoint
	# between the top-left and top-right coordinates, followed by
	# the midpoint between bottom-left and bottom-right coordinates
(tl, tr, br, bl) = box

width, height = height_width_image(tl,tr,br,bl)
xcenter , ycenter = center(tl,tr,br,bl)


xmin = []
xmax = []
ymin = []
ymax = []

xmin.append(tl[0])
xmin.append(tr[0])
xmin.append(br[0])
xmin.append(bl[0])

xmax.append(tl[0])
xmax.append(tr[0])
xmax.append(br[0])
xmax.append(bl[0])

ymax.append(tl[1])
ymax.append(tr[1])
ymax.append(br[1])
ymax.append(bl[1])

ymin.append(tl[1])
ymin.append(tr[1])
ymin.append(br[1])
ymin.append(bl[1])

# x_min_actual = np.min(xmin)
# x_max_acutal = np.max(xmax)
# y_max_actual = np.max(ymax)
# y_min_actual = np.min(ymin)

'''
	'xmin1', 'ymin1', 
    'xmax2', 'ymin2', 
    'xmax3', 'ymax3', 
    'xmin4' , 'ymax4'
'''


xmin_one = np.min(tl[0])/320
ymin_one = np.max(tr[1])/320

xmax_two = np.max(br[0])/320
ymin_two = np.min(bl[1])/320

xmax_three = np.max(tl[0])/320
ymax_three = np.max(tr[1])/320

xmin_four = np.min(br[0])/320
ymax_four = np.max(bl[1])/320

def add_to_csv(label, x_min, x_max, y_min, y_max):
	with open('yolo.csv', 'a', newline='') as csvfile:
		spamwriter = csv.writer(csvfile,delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
		spamwriter.writerow([label, x_min, y_min, x_max, y_max])

def add_label(path,data):
	print("mack ")
	print(path.split("/"))
	label_paths = "../ml/data_export_bricks/labels/"+path.split("/")[2]
	label_file = "../ml/data_export_bricks/labels/"+path.split("/")[2]+"/"+path.split("/")[3]
	os.system("mkdir %s"%(label_paths))
	f = open(label_file, "a")
	f.write(data)
	f.close()

# print("box min and max ", xmin_one," ",ymin_one," ",xmax_two+" ",ymin_two, " ", xmax_three," ",ymax_three, " ", xmin_four," ",xmax_four)

'''
	'xmin1', 'ymin1', 
    'xmax2', 'ymin2', 
    'xmax3', 'ymax3', 
    'xmin4' , 'ymax4'
'''

# x_min = x_min_actual/320
# x_max = (x_max_acutal+width)/320
# y_min = y_min_actual/320
# y_max = (y_max_actual+height)/320
# x_center = (x_min+x_max)/2.
# y_center = (y_min+y_max)/2.
# yolo_x = xcenter/320
# yolo_w = width/320
# yolo_y = ycenter/320
# yolo_h = height/320

# print("YOLO_PARAMS "+str(x_min)+" "+str(y_min)+" "+str(x_max)+" "+str(y_max))

dimA = pixelsPerMetric
dimB = pixelsPerMetric
print("SIZE ", dimA, " ", dimB)
# show the output image
# cv2.imshow("Image", orig)

label_data = args["scale"] +" "+ str(xmin_one)+","+str(ymin_one)+" "+str(xmax_two)+","+str(ymin_two)+" "+str(xmax_three)+","+str(ymax_three)+" "+str(xmin_four)+","+str(ymax_four)
print(label_data)

img_location_loc = "data_export_bricks/images/%s/%s/%s"%(args["label"],str(args["image"]).split("/")[1],str(args["image"]).split("/")[2])
label_location_loc = "data_export_bricks/labels/%s/%s/%s"%(args["label"],str(args["image"]).split("/")[1],str(args["image"]).split("/")[2])
# print("loc ",))
#-p for macos -R for linux for recussive mkdir

imgs = "mkdir -p %s"%(img_location_loc.split("/")[0]+"/"+img_location_loc.split("/")[1]+"/"+img_location_loc.split("/")[2]+"/")
labels = "mkdir -p %s"%(label_location_loc.split("/")[0]+"/"+label_location_loc.split("/")[1]+"/"+label_location_loc.split("/")[2])

os.system(imgs)
os.system(labels)
print("databse data ",imgs)
print("databse data ",labels)

frank_img_label = "data_export_bricks/labels/%s/%s"%(args["label"],label_location_loc.split("/")[4].split(".png")[0]+".txt")
frank_img_path = "data_export_bricks/images/%s/%s"%(args["label"],label_location_loc.split("/")[4])
print("franksss ",frank_img_label)
print("image ",frank_img_path)
touch = "touch %s && echo %s > %s"%(frank_img_label,label_data,frank_img_label)
# print(label_location_loc.split("/")[3])
os.system(touch)
# add_to_csv(label_location_loc.split("/")[3],label_data)
cv2.imwrite(frank_img_path, orig)
# cv2.waitKey(0)