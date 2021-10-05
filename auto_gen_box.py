import os
import csv

labels = []

with open('categories_non_moved.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        img = row[0]
        title = row[1]
        if(title == "Brick"):
            labels.append(img)

with open('part_database_bricks.csv') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    for row in csv_reader:
        save_img = (row[0])
        print("python bounding_box_yolo.py -i %s -w 1 -l %s -s %s"%(save_img,save_img.split("/")[1],labels.index(save_img.split("/")[1])))
        os.system("python bounding_box_yolo.py -i %s -w 1 -l %s -s %s"%(save_img,save_img.split("/")[1],labels.index(save_img.split("/")[1])))
