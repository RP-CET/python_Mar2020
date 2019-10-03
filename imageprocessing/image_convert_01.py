import os
from PIL import Image

where = "img"
outFolder = "out"

def convertImages():
    for root, dirs, files in os.walk(where):
        for file in files:
            fullname = os.path.join(root,file)
            print(fullname)
            if (file.lower().endswith("jpg") or \
                file.lower().endswith("bmp")):
                im = Image.open(fullname)
                f, e = os.path.splitext(file)
                fname2 = f + ".jpg"
                outFilename = os.path.join(outFolder, fname2)
                print(outFilename)
                im.save(outFilename, "jpeg")

convertImages()
