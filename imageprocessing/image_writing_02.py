import os
from PIL import Image, ImageFilter, ImageOps

where = "img"
ext = "jpg"
outFolder = "out"

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

def cleanOutput():
    print("Removing old out files")
    for root, dirs, files in os.walk(outFolder):
        for file in files:
            fullName = os.path.join(root, file)
            os.remove(fullName)
            print(".")

cleanOutput()
processImages()
