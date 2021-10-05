import csv
import os 

with open('categories_non_moved.csv','r') as csv_file:
    csvs = csv.reader(csv_file, delimiter=',')
    for lnm in csvs:
        print("cp -r export_grayscale/%s %s"%(lnm[0],lnm[1]))
        # os.system("cp -r export_grayscale/%s %s"%(lnm[0],lnm[1]))