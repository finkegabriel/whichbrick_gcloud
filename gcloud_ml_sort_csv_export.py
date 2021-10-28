import csv
import subprocess
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-n", "--name", type=str, required=True,
                help="name of the category")
args = vars(ap.parse_args())

'''
,,,,,,,,,
'''

'''
1 we need to list all the files in images/ && labels/
2 match the labels/ to the proper images/ names 
3 list the contents of the label file
4 append all that info to a new CSV

ex:

[set,]image_path[,label,x1,y1,,,x2,y2,,]
TRAIN,gs://My_Bucket/sample1.jpg,cat,0.125,0.25,,,0.375,0.5,,
VALIDATE,gs://My_Bucket/sample1.jpg,cat,0.4,0.3,,,0.55,0.55,,
TEST,gs://My_Bucket/sample1.jpg,dog,0.5,0.675,,,0.75,0.875,,
[set,]image_path[,label,x1,y1,x2,y1,x2,y2,x1,y2]
TRAIN,gs://My_Bucket/sample2.jpg,dog,0.56,0.25,0.97,0.25,0.97,0.50,0.56,0.50

FINAL_RESULT:
TRAIN, gs://whichbrick-2/data_export_bricks/images/LABEL/*.png, LABEL, x1,y1,,,x2,y2,,
'''

'''
automl=pd.DataFrame(columns=['set', 'file', 'label', 
    'xmin1', 'ymin1', 
    'xmax2', 'ymin2', 
    'xmax3', 'ymax3', 
    'xmin4' , 'ymax4'])
'''

PART_NAMES = []
IMG_NAMES = []

LS_ONE = "ls data_export_%s/images/"%(args["name"])

ro = subprocess.check_output(LS_ONE, shell=True).strip()
rl = ro.decode().split('\n')
PART_NAMES.append(rl)
# print(PART_NAMES[0])

for lp in PART_NAMES[0]:
    # print(LS_ONE+lp)
    rt = subprocess.check_output(LS_ONE+lp, shell=True).strip()
    rs = rt.decode().split('\n')
    for lt in rs:
        # print("gs://whichbrick-2/data_export_bricks/images/%s/%s"%(lp,lt))
        LIST_LABELS = "cat impose/data_export_%s/labels/%s/%s"%(args["name"],lp,lt.split(".png")[0]+".txt")
        ry = subprocess.check_output(LIST_LABELS, shell=True).strip()
        ru = ry.decode().split('\n')
        print(ru[0].split(","))
        # 1,2 & 5,6 indexs for bounding boi's
        print("FRIEND!! ",ru[0].split(",")[0].split(" ")[1],ru[0].split(",")[1],ru[0].split(",")[4],ru[0].split(",")[5])
        print("UNASSIGNED","gs://whichbrick-2/data_export_%s/images/%s/%s"%(args["name"],lp,lt),lp,ru[0].split(" ")[1].split(",")[0],ru[0].split(" ")[1].split(",")[1],ru[0].split(" ")[1].split(",")[2],ru[0].split(" ")[1].split(",")[3],ru[0].split(",")[4],ru[0].split(",")[5])
        with open('gcloud_%s.csv'%(args["name"]), 'a', newline='') as csvfile:
            spamwriter = csv.writer(csvfile,delimiter=',')
            for i in range(1,6):
                spamwriter.writerow(["UNASSIGNED","gs://whichbrick-2/data_export_%s/images/%s/%s"%(args["name"],lp,lt.split('.png')[0]+'_%s'%(i)+'.png'),lp,ru[0].split(" ")[1].split(",")[0],ru[0].split(" ")[1].split(",")[1],ru[0].split(" ")[1].split(",")[2],ru[0].split(" ")[1].split(",")[3],ru[0].split(",")[4],ru[0].split(",")[5],'','',])