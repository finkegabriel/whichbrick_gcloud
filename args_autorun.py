import os
import csv

with open('cats.csv') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    for row in csv_reader:
        save_img = (row[0])
        print("python auto_gen_box.py -n %s"%(save_img))
        os.system("python auto_gen_box.py -n %s"%(save_img))
