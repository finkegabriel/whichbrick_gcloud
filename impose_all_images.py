import os
import csv
import argparse

labels = []

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--path", type=str, required=True,
                help="path name")
args = vars(ap.parse_args())

with open('backgrounds.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        path = row[0].split('/')
        label = args["path"].split('/')
        labels = "impose/"+str(label[0])+"/"+str(label[1])+"/"+str(label[2])
        image = str(label[0])+"/"+str(label[1])+"/"+str(label[2])+"/"+str(label[3])
        data_output = str(image.split('/')[3])
        real_image = (data_output.split('.')[0])+'_'+path[1].split('.')[0]+'.png'
        os.system("mkdir -p %s"%(labels))
        os.system("python make_transparent.py -i %s -o %s"%(image,labels+"/"+real_image))
        print("\n")
        os.system("python overlay_image.py -b %s -o %s -n %s"%(row[0],labels+"/"+real_image,labels+"/"+real_image))

