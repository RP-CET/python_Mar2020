import os

where = "img"

def searchByExtension(ext):
    c = 1
    for root, dirs, files in os.walk(where):
        for file in files:
            fullname = os.path.join(root, file)
            if file.endswith(ext):
                print ("%2d %s" % (c, fullname))
                c += 1

searchByExtension("jpg")


