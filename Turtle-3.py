import turtle
win = turtle.Screen()
win.screensize(500,500)
win.title("spiral")
win.bgcolor("black")

t = turtle.Turtle()
t.color("gold")

for i in range(200):
    t.forward(i*3)
    t.right(90)

turtle.done() 