import turtle
colors = ['red','yellow','blue','orange','green','purple']
# sides=6
# changes 6 down to 2
s = input("Enter a number of sides between 2 and 6:  ")
sides = int(s)
t=turtle.Pen()
turtle.bgcolor("black")
for x in range(360):
    t.pencolor(colors[x%sides])
    t.forward(x * 3/sides + x)
    t.left(360/sides + 1)
    t.width(x*sides/200)
