import turtle
win = turtle.Screen()
win.screensize(500,500)
win.title("Star")
win.bgcolor("skyblue")

t = turtle.Turtle()
t.color("red")
n = 6
for i in range(3):
    t.forward(100)
    t.left(360/3)
t.left(90)
t.penup()
t.forward(60)
t.pendown()
t.right(90)
for i in range(3):
    t.forward(100)
    t.right(360/3)
turtle.done()