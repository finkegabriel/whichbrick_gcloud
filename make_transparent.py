from PIL import Image
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="path to the input image")
ap.add_argument("-o", "--output", required=True,
                help="name of output image")
args = vars(ap.parse_args())

def convertImage(image,output):
    img = Image.open(image)
    img = img.convert("RGBA")
  
    datas = img.getdata()
  
    newData = []
  
    for items in datas:
        if items[0] == 255 and items[1] == 255 and items[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(items)
  
    img.putdata(newData)
    img.save(output, "PNG")
    print("Successful")

convertImage(args["image"],args["output"])