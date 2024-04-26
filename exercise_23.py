from turtle import Turtle
t = Turtle()
for i in range(3,9) :
    angle = 360/i
    for _ in range(i) : 
        t.forward(100)
        t.rt(angle)
t.screen.mainloop()