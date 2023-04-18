from turtle import Turtle, done

t = Turtle()
t.screen.bgcolor('black')
t.pencolor('red')
t.fillcolor('yellow')
t.begin_fill()

t.shape('turtle')
# for i in range(5):
#     t.forward(100)
#     t.right(144)

# for i in range(360):
#     t.forward(1)
#     t.right(1)
for i in range(6):
    t.forward(100)
    t.right(60)


t.end_fill()

done()