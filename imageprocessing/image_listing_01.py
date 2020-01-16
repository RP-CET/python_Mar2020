import os

where = "img"
ext = "jpg"

def processImages():
    c = 1
    for root, dirs, files in os.walk(where):
        for file in files:
            fullname = os.path.join(root, file)
            if file.endswith(ext):
                print ("%2d %s" % (c, fullname))
                c += 1

processImages()


