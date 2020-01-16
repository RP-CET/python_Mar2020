import os
from PIL import Image, ImageFilter, ImageOps, ImageEnhance

where = "img"
ext = "jpg"

def processImages():
    c = 1
    for root, dirs, files in os.walk(where):
        for file in files:
            fullname = os.path.join(root, file)
            if file.endswith(ext):
                im = Image.open(fullname)
                print ("%2d %s %s (%s)" \
                       % (c, fullname, im.size, im.mode))
                enh = ImageEnhance.Contrast(im)
                out = enh.enhance(1.3)
                out.show()
                c += 1
                break

processImages()
