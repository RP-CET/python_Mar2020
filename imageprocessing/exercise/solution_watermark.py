import os
from PIL import Image, ImageOps

def watermark(im, mark, position):
    layer = Image.new("RGBA", im.size, (0,0,0,0))
    layer.paste(mark, position)
    return Image.composite(layer, im, layer)

if os.path.isdir("processed") == False:
    os.makedirs("processed")

where = "src"
ext = "jpg"

def processImages():
    c = 1
    for root, dirs, files in os.walk(where):
        for file in files:
            fullname = os.path.join(root, file)
            if file.endswith(ext):
                im = Image.open(fullname)
                out = ImageOps.grayscale(im)

                final = watermark(out, mark, (700, 500))

                outFilename = os.path.join("processed", file)
                final.save(outFilename)
                c += 1



mark = Image.open("src/similan.jpg")
mark = mark.resize((100,100))

processImages()






