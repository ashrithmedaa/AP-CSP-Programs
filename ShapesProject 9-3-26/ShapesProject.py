#Ashrith Meda, Turtle Project 9/3/26
import turtle
t = turtle.Turtle()
#Screen Setup
screen = turtle.Screen()
screen.setup(1000,1000)
#Start of the rectangle drawing + fill
t.color("blue")
t.begin_fill()
t.forward(300)
t.left(90)
t.forward(100)
t.left(90)
t.forward(300)
t.left(90)
t.forward(100)
t.end_fill()
t.pu()
#Start of the triangle + fill
t.color("blue")
t.begin_fill()
t.left(270)
t.forward(150)
t.forward(200)
t.pd()
for i in range(3):
    t.forward(120)
    t.left(120)
t.end_fill()
#Start of the Circle + fill
t.penup()
t.right(90)
t.forward(150)
t.pd()
t.dot(100,"blue")


