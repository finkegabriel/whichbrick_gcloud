import csv
from PIL import Image
import cv2
import numpy as np
import os

with open('part_database.csv') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    for row in csv_reader:
        # print("mkdir export_grayscale/%s"%(row[1].split("/")[1]))
        # os.system("mkdir export_grayscale/%s"%(row[1].split("/")[1]))
        image_current = row[0]
        img = Image.open(image_current).convert('LA')
        image = cv2.imread("%s"%(image_current))
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        img2 = np.zeros_like(image)
        img2[:,:,0] = gray
        img2[:,:,1] = gray
        img2[:,:,2] = gray
        save_img = ("export_grayscale/%s/%s"%(row[1].split("/")[1],row[0].split("/")[3]))
        print(save_img)
        cv2.imwrite(save_img,img2)