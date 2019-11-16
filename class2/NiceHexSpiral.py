#NiceHexSpiral.py
import turtle   
colors=['pink', 'green', 'yellow', 'orange', 'red', 'blue']
t=turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x/100+1)
    t.forward(x)        
    t.left(59)
