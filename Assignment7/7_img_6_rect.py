from images import Image

img = Image('myImage.gif')

yellow = (255,255,0)
for x in range(320,520):
    for y in range(200,300):
        img.setPixel(x,y,yellow)
img.draw()