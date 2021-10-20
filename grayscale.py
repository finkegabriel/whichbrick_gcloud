import csv
from PIL import Image
import cv2
import numpy as np
import os

# with open('csv/part_database.csv') as csv_file:
# csv_reader = csv.reader(csv_file,delimiter=';')
# for row in csv_reader:
# print("mkdir export_grayscale/%sldr"%(row[2].split("/")[0]))
# os.system("mkdir export_grayscale/%sldr" % (row[2].split("/")[0]))
image_current = "backgrounds/5.jpg"
# print(image_current)
img = Image.open(image_current).convert('LA')
image = cv2.imread("%s" % (image_current))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
img2 = np.zeros_like(image)
img2[:, :, 0] = gray
img2[:, :, 1] = gray
img2[:, :, 2] = gray
# print(row[2])
# save_img = ("export_grayscale/"+row[2]+"ldr/"+row[0]).split("/")
# save_img_actutal = save_img[0]+"/"+save_img[1]+"/"+save_img[4]
# print(save_img)
cv2.imwrite("backgrounds/5.png", img2)
