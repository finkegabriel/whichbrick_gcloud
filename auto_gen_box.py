import os
import csv
import argparse

labels = []

ap = argparse.ArgumentParser()
ap.add_argument("-n", "--name", type=str, required=True,
                help="name of the category")
args = vars(ap.parse_args())


with open('categories_non_moved.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        img = row[0]
        title = row[1]
        if(title == args["name"]):
            labels.append(img)

with open('part_database.csv') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    for row in csv_reader:
        save_img = (row[0])
        # print(save_img.split("/")[1])
        print("python bounding_box_yolo.py -i %s -w 1 -l %s -n %s"%(save_img,save_img.split("/")[1],save_img.split("/")[0]))
        # print("python bounding_box_yolo.py -i %s -w 1 -l %s -n %s"%(save_img,save_img.split("/")[1],labels.index(save_img.split("/")[1])))
        os.system("python bounding_box_yolo.py -i %s -w 1 -l %s -n %s"%(save_img,save_img.split("/")[1],save_img.split("/")[0]))#,labels.index(save_img.split("/")[1])))
