from turtle import Turtle, done
def polygon(t,poly):
    t.up()
    x,y=poly[-1]
    t.goto(x,y)
    t.down()
    t.fillcolor('yellow')
    t.pencolor('black')
    t.begin_fill()
    for x,y in poly:
        t.goto(x,y)
    t.end_fill()
t= Turtle()
poly=[(0,0),(150,100),(200,250),(-110,150),(0,0)]
polygon(t,poly)

done()