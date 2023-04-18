from images import Image

img = Image(400, 400)

# Diagonal
y = 0
for x in range(int(img.getWidth())):
    img.setPixel(x, y, (0,0,255))
    y+=1
img.draw()

# Horizontal
y = img.getHeight() // 2
for x in range(int(img.getWidth())):
    img.setPixel(x, y, (0,0,255))
img.draw()