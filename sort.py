import os
import csv
import re
import subprocess

pipe = []

def dirs():
    with open('../../webscrape/scrape_for_csv/output.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            res = re.findall("(Animal|Antenna|Arch|Arm|Bar|Baseplate|Belville|Boat|Bracket|Brick|Car|Clikits|Cockpit|Cone|Constraction|Constraction|Accessory|Container|Conveyor|Crane|Cylinder|Dish|Door|Electric|Exhaust|Fence|Figure|Figure Accessory|Flag|Forklift|Freestyle|Garage|Glass|Grab|Hinge|Homemaker|Hose|Ladder|Lever|Magnet|Minifig|Minifig Accessory|Minifig Footwear|Minifig Headwear|Minifig Hipwear|Minifig Neckwear|Monorail|Obsolete|Panel|Plane|Plant|Plate|Platform|Propeller|Rack|Road|sign|Rock|Scala|Screw|Sheet Cardboard|Sheet Fabric|Sheet Plastic|Slope|Sphere|Staircase|Sticker|Support|Tail|Tap|Technic|Tile|Tipper|Tractor|Trailer|Train|Turntable|Tyre|Vehicle|Wedge|Wheel|Winch|Window|Windscreen|Wing|Znap)+",row[1])
            if len(res) != 0:
                try:
                    subprocess.check_output(('mkdir %s'%(res[0])), shell=True)
                    break
                except:
                    print("error")

dirs()