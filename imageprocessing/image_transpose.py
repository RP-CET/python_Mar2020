import os
from PIL import Image, ImageFilter, ImageOps

where = "img"
outFolder = "out"

def processAllImage(onlyFirst):
    c = 1
    for root, dirs, files in os.walk(where):
        for file in files:
            fullname = os.path.join(root, file)
            if file.lower().endswith("jpg") or \
                    file.lower().endswith("bmp") or \
                    file.lower().endswith("png") or \
                    file.lower().endswith("svg"):
                im = Image.open(fullname)
                outFilename = os.path.join(outFolder,file)
                print ("%2d %s %s (%s)" \
                       % (c, fullname, im.size, im.mode))

                out = im.transpose(Image.FLIP_LEFT_RIGHT)
                im.show()
                out.show()
                out.save(outFilename)
                c += 1
                if (onlyFirst):
                    return

def cleanOutput():
    print("Removing old out files")
    for root, dirs, files in os.walk(outFolder):
        for file in files:
            fullName = os.path.join(root, file)
            os.remove(fullName)
            print(".")

cleanOutput()
processAllImage(True)
