import turtle
t=turtle.Pen()
turtle.bgcolor("black")
colors = ['red','yellow','blue','orange','green','purple']
# your_name=t.textinput("Enter your name", "What is your name?")
your_name="Tom"
for x in range(100):
    t.pencolor(colors[x%6])
    t.penup()
    t.forward(x*4)
    t.pendown()
    t.write(your_name,font=("Arial",int((x+4)/4),"bold"))
    t.left(92)
