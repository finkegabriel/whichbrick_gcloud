import os
import csv

lables = []

with open('categories_non_moved.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        img = row[0]
        title = row[1]
        if(title == "Brick"):
            lables.append(img)
            print(img,title)

f = open("yolo.yml", "a")
f.write('''
    # train and val data as 1) directory: path/images/, 2) file: path/images.txt, or 3) list: [path1/images/, path2/images/]
    train: data/images
    val: data/images
    
    # number of classes
    nc: %s

    # class names
    names: %s
            '''%(len(lables),lables))
f.close()