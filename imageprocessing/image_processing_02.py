import os
from PIL import Image, ImageFilter, ImageOps

where = "img"
ext = "jpg"

def processImages():
    c = 1
    for root, dirs, files in os.walk(where):
        for file in files:
            fullname = os.path.join(root, file)
            if file.endswith(ext):
                im = Image.open(fullname)
                print ("%2d %s %s (%s)" % \
                       (c, fullname, im.size, im.mode))
                #out = im.filter(ImageFilter.BLUR)
                #out = im.filter(ImageFilter.FIND_EDGES)
                #out = im.filter(ImageFilter.CONTOUR)
                #out = ImageOps.grayscale(im)
                out = ImageOps.solarize(im)
                out.show()
                c += 1
                break

processImages()
