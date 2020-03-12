import os
from PIL import Image, ImageFilter, ImageOps

where = "img"
ext = "jpg"
outFolder = "output"

if os.path.isdir("output") == False:
    os.makedirs("output")

def processImages():
    c = 1
    for root, dirs, files in os.walk(where):
        for file in files:
            fullname = os.path.join(root, file)
            if file.endswith(ext):
                im = Image.open(fullname)
                outFilename = os.path.join(outFolder,file)
                print ("%2d %s %s (%s)" % \
                       (c, fullname, im.size, im.mode))
                out = im.filter(ImageFilter.BLUR)
                #out.show()
                out.save(outFilename)
                c += 1
                break

processImages()

