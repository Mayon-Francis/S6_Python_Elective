from images import Image

img = Image('myImage.gif')
black = (0,0,0)
white = (255,255,255)
threshold = 250

for y in range(img.getHeight()):
    for x in range(img.getWidth()):
        (r,g,b) = img.getPixel(x,y)
        avg = r+g+b // 3
        if avg < threshold:
            img.setPixel(x,y,black)
        else:
            img.setPixel(x,y,white)

img.draw()