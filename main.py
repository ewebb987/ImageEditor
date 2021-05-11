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
    print("Processing - " + file)

    backImage = Image.open(dirname + "\\background.png").convert("RGB")
    mainImage = resizeImg(Image.open(inputDirectory + "\\" + file))

    newImage = backImage.copy()
    newImage.paste(mainImage,(calcOffset(mainImage),0))
    newImage.save(outputDirectory + "\\" + file)

    print("Success - " + file)
