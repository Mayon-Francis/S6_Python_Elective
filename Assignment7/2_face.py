from turtle import Turtle, done

t = Turtle()
t.speed(0)

# Circle
start = (0,0)
lineLength = 30
radius = 100
t.up()
t.goto(start[0], start[1] - radius)
t.down()
t.circle(100)

# Nose
t.up()
t.goto(start[0], start[1] - lineLength//2 - 20)
t.down()
t.left(90)
t.forward(lineLength)

# Eyebrows
t.up()
t.forward(20)
t.left(90)
t.forward(lineLength + 20)
t.right(180)
t.down()
t.forward(lineLength)
t.up()
t.forward(40)
t.down()
t.forward(lineLength)

# Left eye
t.up()
t.right(180)
t.forward(lineLength//2)
t.left(90)
t.forward(20)
t.down()
t.dot(10)

# Right eye
t.up()
t.right(90)
t.forward(lineLength + 40)
t.dot(10)

# Mouth
t.up()
t.goto(start[0]+lineLength*0.75, start[1] - radius //2)
t.down()
t.forward(lineLength*1.5)

t.hideturtle()
done()