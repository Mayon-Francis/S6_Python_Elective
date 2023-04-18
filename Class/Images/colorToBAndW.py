from images import Image

img = Image('cat.gif')
black = (0,0,0)
white = (255,255,255)

for y in range(img.getHeight()):
    for x in range(img.getWidth()):
        (r,g,b) = img.getPixel(x,y)
        avg = r+g+b // 3
        if avg < 128:
            img.setPixel(x,y,black)
        else:
            img.setPixel(x,y,white)

img.draw()