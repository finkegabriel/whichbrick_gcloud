import csv
import re

x = ""

with open('../categories_final.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar=' ')
    for list in spamreader:
        x = re.findall("(Animal|Antenna|Arch|Arm|Bar|Baseplate|Belville|Boat|Bracket|Brick|Car|Clikits|Cockpit|Cone|Constraction|Constraction|Accessory|Container|Conveyor|Crane|Cylinder|Dish|Door|Electric|Exhaust|Fence|Figure|Figure Accessory|Flag|Forklift|Freestyle|Garage|Glass|Grab|Hinge|Homemaker|Hose|Ladder|Lever|Magnet|Minifig|Minifig Accessory|Minifig Footwear|Minifig Headwear|Minifig Hipwear|Minifig Neckwear|Monorail|Obsolete|Panel|Plane|Plant|Plate|Platform|Propeller|Rack|Road|sign|Rock|Scala|Screw|Sheet Cardboard|Sheet Fabric|Sheet Plastic|Slope|Sphere|Staircase|Sticker|Support|Tail|Tap|Technic|Tile|Tipper|Tractor|Trailer|Train|Turntable|Tyre|Vehicle|Wedge|Wheel|Winch|Window|Windscreen|Wing|Znap)+",list[1])
        if(len(x) !=0):
            print(list[0],x[0])
            with open('categories_non_moved.csv','a', newline='') as csvfile:
                writer = csv.writer(csvfile,delimiter=',')
                writer.writerow([list[0],x[0]])
        else:
            with open('categories_final_moved.csv','a', newline='') as csvfile:
                writer = csv.writer(csvfile,delimiter=',')
                # print(list[0],list[1])
                list_one = str(list[0])
                list_two = str(list[1])
                writer.writerow([(list_one),(list_two)])


