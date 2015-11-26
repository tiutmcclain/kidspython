#!/usr/bin/python
import turtle
t = turtle.Pen()
t.pencolor("red")
for x in range(4):
   t.circle(100)
   t.left(90)
t.penup()
t.forward(5)
t.pendown()
# Rosette 6
t.pencolor("black")
for x in range(6):
    t.circle(100)
    t.left(60)
