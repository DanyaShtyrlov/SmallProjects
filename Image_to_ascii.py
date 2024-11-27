import sys
from PIL import Image
"@, #, 0, ., 1, ,"
def decide_sighn(B):
    if B < 51 and B >= 0:
        return "@"
    elif B < 102 and B >= 51:
        return "#"
    elif B < 156 and B >= 102:
        return "0"
    elif B < 205 and B >= 156:
        return "1"
    elif B <= 256 and B >= 205:
        return "."


arguments = sys.argv
with Image.open(arguments[1]) as image:
    image.load()

image.convert("RGB")

file = open(arguments[2], "w")

height, width = image.size
for i in range(width):
    for j in range(height):
        R,G,B = image.getpixel([j,i])
        Brightness = (R + G + B) // 3 
        file.write(decide_sighn(Brightness))
    file.write("\n")