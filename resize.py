from PIL import Image

size = 320, 320
im = Image.open("2.png")
im_resized = im.resize(size, Image.ANTIALIAS)
im_resized.save("2.png", "PNG")