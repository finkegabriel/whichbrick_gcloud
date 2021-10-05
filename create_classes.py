import os
import subprocess
import csv

files = []
fil = "ls data_export/images"
ro = subprocess.check_output(fil, shell=True).strip()
rl = ro.decode().split('\n')
files.append(rl)
with open('yolos.csv', 'a', newline='') as csvfile:
    spamwriter = csv.writer(csvfile,delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for d in files[0]:
        spamwriter.writerow([d])

print(files[0])