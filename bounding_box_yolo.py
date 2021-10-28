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
ap.add_argument("-n", "--name", type=str, required=True,
                help="name of the category")
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
orig = image.copy()

def square(cnts):
	for c in cnts:
		# if the contour is not sufficiently large, ignore it
		if cv2.contourArea(c) < 100:
			continue
	# compute the rotated bounding box of the contour
	# box = cv2.boxPoints(rect)
	# box = np.int0(box)
	# box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
	# order the points in the contour such that they appear
	# in top-left, top-right, bottom-right, and bottom-left
	# order, then draw the outline of the rotated bounding
	# box
	# Uncomment if you want bounding boi's around your img
		x,y,w,h = cv2.boundingRect(c)
		print("two flat ",x,y,w,h)
		orig = image.copy()
		box = cv2.minAreaRect(c)
		box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
		box = np.array(box, dtype="int")
	# order the points in the contour such that they appear
	# in top-left, top-right, bottom-right, and bottom-left
	# order, then draw the outline of the rotated bounding
	# box
		box = perspective.order_points(box)
		return x,y,w,h
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
(tl, tr, br, bl) = square(cnts)
x,y,w,h = square(cnts)
cv2.rectangle(orig,(x,y),(x+w,y+h),(0,255,0),2)

print("box ",tl,tr,br,bl)

#The bellow cords. are a function of the image size and the width of the object
# print("BOXING BOXES BOI's ","\n",
# (tl[0]/320),"\n",
# (tl[1]/320),"\n",
# (tr[0]/320),"\n",
# (tr[1]/320),"\n",
# (br[0]/320),"\n",
# (br[1]/320),"\n",
# (bl[0]/320),"\n",
# (bl[1]/320))

# width, height = height_width_image(tl,tr,br,bl)
# xcenter , ycenter = center(tl,tr,br,bl)

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


# xmin_one = np.min(tl[0])
# ymin_one = np.max(tr[1])

# xmax_two = np.max(br[0])/320
# ymin_two = np.min(bl[1])/320

# xmax_three = np.max(tl[0])/320
# ymax_three = np.max(tr[1])/320

# xmin_four = np.min(br[0])/320
# ymax_four = np.max(bl[1])/320

# cv2.putText(orig,("%s,%s"%(tl[0]/100,tl[1]/100)), (int(tl[0]),int(tl[1])), 0, 1, 255)
# cv2.putText(orig,("%s,%s"%(br[0]/100,br[1]/100)), (int(br[0]),int(br[1])), 0, 1, 255)

def add_to_csv(label, x_min, x_max, y_min, y_max):
	with open('yolo.csv', 'a', newline='') as csvfile:
		spamwriter = csv.writer(csvfile,delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
		spamwriter.writerow([label, x_min, y_min, x_max, y_max])

def add_label(path,data):
	print("mack ")
	print(path.split("/"))
	label_paths = "../ml/data_export_animal/labels/"+path.split("/")[2]
	label_file = "../ml/data_export_animal/labels/"+path.split("/")[2]+"/"+path.split("/")[3]
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

#create square out of rectangle
print("rectangle ",tl/320,"  ")

label_data = args["name"] +" "+str(x/320)+","+str(y/320)+",,,"+str((x+w)/320)+","+str((y+h)/320)+",,"
# label_data = args["name"] +" "+ str(xmin_one)+","+str(ymin_one)+","+str(xmax_two)+","+str(ymin_two)+","+str(xmax_three)+","+str(ymax_three)+","+str(xmin_four)+","+str(ymax_four)
print(label_data)

img_location_loc = "data_export_%s/images/%s/%s/%s"%(args["name"],args["label"],str(args["image"]).split("/")[1],str(args["image"]).split("/")[2])
label_location_loc = "data_export_%s/labels/%s/%s/%s"%(args["name"],args["label"],str(args["image"]).split("/")[1],str(args["image"]).split("/")[2])
# print("loc ",))
#-p for macos -R for linux for recussive mkdir


#TODO append impose/to the front of this command in order to place the labels in the right places 
imgs = "mkdir -p %s"%(img_location_loc.split("/")[0]+"/"+img_location_loc.split("/")[1]+"/"+img_location_loc.split("/")[2]+"/")
labels = "mkdir -p %s"%('impose/'+label_location_loc.split("/")[0]+"/"+label_location_loc.split("/")[1]+"/"+label_location_loc.split("/")[2]+"/")

print(imgs)
print(labels)
os.system(imgs)
os.system(labels)
print("databse data ",imgs)
print("databse data ",labels)

frank_img_label = "impose/data_export_%s/labels/%s/%s"%(args["name"],args["label"],label_location_loc.split("/")[4].split(".png")[0]+".txt")
frank_img_path = "data_export_%s/images/%s/%s"%(args["name"],args["label"],label_location_loc.split("/")[4])
print("franksss ",frank_img_label)
print("image ",frank_img_path)
touch = "touch %s && echo %s > %s"%(frank_img_label,label_data,frank_img_label)
# print(label_location_loc.split("/")[3])

#### Touch's files and echos data to it
os.system(touch)

# add_to_csv(label_location_loc.split("/")[3],label_data)

###### Write the image to filesystem
cv2.imwrite(frank_img_path, orig)

# cv2.imshow("preview ",orig)
# cv2.waitKey(0)
os.system("python impose_all_images.py -p %s"%(frank_img_path))