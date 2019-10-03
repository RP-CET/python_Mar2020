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

                out = im.filter(ImageFilter.BLUR)
                im.show()
                out.show()
                out.save(outFilename)
                c += 1
                if (onlyFirst):
                    return

processAllImage(True)
