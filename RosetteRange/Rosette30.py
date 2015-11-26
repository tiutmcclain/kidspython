#!/usr/bin/python
import turtle
t = turtle.Pen()
t.pencolor("red")
num_circle = 30
for x in range(num_circle):
   t.circle(100)
   t.left(360/num_circle)
