from turtle import Turtle, Screen
s1 = Screen()
t = Turtle()
def forward() :
    t.setheading(0)
    t.forward(100)
def backward() :
    t.setheading(180)
    t.forward(100)
def pressL() :
    t.lt(8)
    t.forward(16)
def pressA() :
    t.rt(8)
    t.forward(16)

s1.listen()
s1.onkey(fun=forward,key="Right")
s1.onkey(fun=backward,key="Left")
s1.onkey(fun=pressL,key="l")
s1.onkey(fun=pressA,key="a")
s1.exitonclick()
