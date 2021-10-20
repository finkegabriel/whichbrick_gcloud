from PIL import Image

size = 320, 320
im = Image.open("backgrounds/5.png")
im_resized = im.resize(size, Image.ANTIALIAS)
im_resized.save("backgrounds/5.png", "PNG")