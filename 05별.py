import turtle
turtle.Screen().setup(0.3, 0.3)
t = turtle.Turtle()
t.shape('turtle')

t.speed(2)
t.penup()
t.goto(-150,0)
t.pendown()
t.color('red')
t.begin_fill()
for i in range(5):
    t.forward(100)
    t.left(144)

t.end_fill()

t.ht()
