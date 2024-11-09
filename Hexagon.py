import turtle
win = turtle.Screen()
win.screensize(500,500)
win.title("Hexagon")
win.bgcolor("skyblue")

t = turtle.Turtle()
t.color("cyan")
n = 6
for i in range(6):
    t.forward(100)
    t.right(360/6)
turtle.done()