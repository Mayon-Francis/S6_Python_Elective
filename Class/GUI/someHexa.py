from turtle import Turtle, done

side = 100
count = 5
t = Turtle()
for i in range(count):
    for _ in range(count):
        t.circle(side/2)
        t.left(360/count)
    t.left(90)
    t.up()
    t.forward(side/2)
    t.right(90)
    t.down()


done()