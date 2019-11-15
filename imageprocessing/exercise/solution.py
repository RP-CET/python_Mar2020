import os
from PIL import Image, ImageFilter, ImageOps

if os.path.isdir("processed") == False:
    os.makedirs("processed")

where = "src"

def processAllImage():
    c = 1
    for root, dirs, files in os.walk(where):
        for file in files:
            fullname = os.path.join(root, file)
            if file.lower().endswith("jpg") :
                im = Image.open(fullname)
                print ("%2d %s %s (%s)" % (c, fullname, im.size, im.mode))
                out = ImageOps.grayscale(im)
                c += 1
                outFilename = os.path.join("processed", file)
                out.save(outFilename)


processAllImage()
