import csv
import sys
import re
import subprocess

chunkS = 0
x = []
l = []
y = []
superList = []
aa = []
arr = []

def chunkCSV():
    files = ("ls hold_this")
    result = subprocess.check_output(files, shell=True).strip()
    ses = result.decode().split('\n')
    for ls in (ses):
        with open('part_database.csv','a',newline='') as csv_f:
            writer = csv.writer(csv_f,delimiter=';')
            fil = ("ls %s"%(ls))
            ro = subprocess.check_output(fil, shell=True).strip()
            rl = ro.decode().split('\n')
            if(rl[0] != ''):
                print()
                for rs in rl:
                    lists = subprocess.check_output(("ls %s/%s"%(ls,rs)), shell=True).strip()
                    rlst = lists.decode().split('\n')
                    for lmt in rlst:
                        print("%s/%s/%s"%(ls,rs,lmt))
                        writer.writerow(["%s/%s/%s"%(ls,rs,lmt)])

arg = sys.argv[1]
if arg == 'chunk':
    chunkCSV()