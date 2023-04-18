from images import Image

img = Image('cat.gif')
black = (0,0,0)
white = (255,255,255)

# Luminance
# Y = 0.299 R + 0.587 G + 0.114 B
# https://stackoverflow.com/questions/596216/formula-to-determine-perceived-brightness-of-rgb-color
for y in range(img.getHeight()):
    for x in range(img.getWidth()):
        (r,g,b) = img.getPixel(x,y)
        r = r * 0.299
        g = g * 0.587
        b = b * 0.114
        avg = int(r+g+b)
        img.setPixel(x,y,(avg,avg,avg))

img.draw()