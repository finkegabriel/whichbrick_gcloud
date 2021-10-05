import csv
import subprocess

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

LS_ONE = "ls data_export_bricks/images/"

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
        LIST_LABELS = "cat data_export_bricks/labels/%s/%s"%(lp,lt.split(".png")[0]+".txt")
        ry = subprocess.check_output(LIST_LABELS, shell=True).strip()
        ru = ry.decode().split('\n')
        print(ru[0].split(","))
        print("UNASSIGNED","gs://whichbrick-2/data_export_bricks/images/%s/%s"%(lp,lt),lp,ru[0].split(" ")[1].split(",")[0],ru[0].split(" ")[1].split(",")[1],ru[0].split(" ")[1].split(",")[2],ru[0].split(" ")[1].split(",")[3],ru[0].split(" ")[1].split(",")[4],ru[0].split(" ")[1].split(",")[5],ru[0].split(" ")[1].split(",")[6],ru[0].split(" ")[1].split(",")[7])
        with open('gcloud_bricks.csv', 'a', newline='') as csvfile:
            spamwriter = csv.writer(csvfile,delimiter=',')
            spamwriter.writerow(["UNASSIGNED","gs://whichbrick-3/data_export_bricks/images/%s/%s"%(lp,lt),lp])#,ru[0].split(" ")[1].split(",")[0],ru[0].split(" ")[1].split(",")[1],ru[0].split(" ")[1].split(",")[2],ru[0].split(" ")[1].split(",")[3],ru[0].split(" ")[1].split(",")[4],ru[0].split(" ")[1].split(",")[5],ru[0].split(" ")[1].split(",")[6],ru[0].split(" ")[1].split(",")[7]])