# drwaw dotted line. by turtle module.
from turtle import Turtle
t = Turtle()
t.shape("circle")
for i in range (0,10,1) :
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()
    t.forward(10)
t.screen.mainloop()