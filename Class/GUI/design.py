import turtle
def drawPoints( t,xc,yc,x,y):
 t.up()
 t.setpos(xc+x, yc+y)
 t.down()
 t.dot(5)
 t.up()
 t.setpos(xc-x, yc+y)
 t.down()
 t.dot(5)
 t.up()
 t.setpos(xc+x, yc-y)
 t.down()
 t.dot(5)
 t.up()
 t.setpos(xc-x, yc-y)
 t.down()
 t.dot(5)
 t.up()
 t.setpos(xc+y, yc+x)
 t.down()
 t.dot(5)
 t.up()
 t.setpos(xc-y, yc+x)
 t.down()
 t.dot(5)
 t.up()
 t.setpos(xc+y, yc-x)
 t.down()
 t.dot(5)
 t.up()
 t.setpos(xc-y, yc-x)
 t.down()
 t.dot(5)
# Function for circle-generation using Bresenham's algorithm
def circleBres(t,xc,yc,r):
 x = 0
 y = r
 d = 3 - 2 * r
 while x<=y :
    drawPoints(t,xc, yc, x, y)
    x=x+1
    if d>0:
        y=y-1
        d=d+4*(x-y)+10
    else:
        d=d+4*x+6

t=turtle.Turtle()
circleBres(t,0,0,50)
t.hideturtle()

turtle.done()