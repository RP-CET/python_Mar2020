import os

where = "img"

def processAllImage():
    c = 1
    for root, dirs, files in os.walk(where):
        for file in files:
            fullname = os.path.join(root, file)
            if file.lower().endswith("jpg") or \
                    file.lower().endswith("bmp") or \
                    file.lower().endswith("png") or \
                    file.lower().endswith("svg"):
                print ("%2d %s" % (c, fullname))
                c += 1

processAllImage()


