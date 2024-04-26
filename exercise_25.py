from turtle import Turtle,Screen
s1 = Screen()
t = Turtle()
t.color("orange","yellow")
print(t.heading())
t.speed("fast")
t.begin_fill()
for i in range(100) :  
    t.forward(200)
    t.lt(170)
    if t.heading() == 0 :
        break
t.end_fill()
s1.exitonclick()
s2 = Screen()
t1 = Turtle()
t1.forward(100)
s2.exitonclick()