from PIL import Image

size = 320, 320
im = Image.open("arg.png")
im_resized = im.resize(size, Image.ANTIALIAS)
im_resized.save("resized_images/args2.png", "PNG")