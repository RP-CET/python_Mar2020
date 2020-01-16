import os
from PIL import Image

where = "img"
ext = "png"
outFolder = "out"

def convertImages():
    for root, dirs, files in os.walk(where):
        for file in files:
            fullname = os.path.join(root,file)
            print("original : " + fullname)
            if file.endswith(ext):
                im = Image.open(fullname)
                f, e = os.path.splitext(file)
                fname2 = f + ".jpg"
                outFilename = os.path.join(outFolder, fname2)
                print("new : " + outFilename)
                im.save(outFilename, "jpeg")

convertImages()
