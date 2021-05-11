import os
from PIL import Image

SET_HEIGHT = 900
SET_WIDTH = 1600
RADIAL_WIDTH = round(SET_WIDTH/2)

def resizeImg(image):
    width = int(image.size[0])
    ratio = float(int(image.size[1])/width)
    calcWidth = (SET_HEIGHT / ratio)
    return image.resize((round(calcWidth),SET_HEIGHT), Image.ANTIALIAS)

def calcOffset(image):
    radialWidth = round(int(image.size[0])/2)
    return RADIAL_WIDTH - radialWidth

dirname, filename = os.path.split(os.path.abspath(__file__))

outputDirectory = dirname + "\\output"
inputDirectory = dirname + "\\input"

files = os.listdir(inputDirectory)
for file in files:
    fileName = str(file)
    print("Processing - " + fileName)

    img1 = Image.open(dirname + "\\background.png")
    _img1 = img1.convert("RGB")

    img2 = Image.open(inputDirectory + "\\" + fileName)
    _img2 = resizeImg(img2)

    backImage = _img1.copy()
    backImage.paste(_img2,(calcOffset(_img2),0))
    backImage.save(outputDirectory + "\\" + fileName)

    print("Success - " + fileName)



