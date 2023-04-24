from turtle import Turtle, done

t=Turtle()
t.left(180)

side = 100
angle = 60
t.color("red", "yellow")
t.begin_fill()
for i in range(6):
    t.forward(100)
    t.right(angle)
    
t.end_fill()
done()