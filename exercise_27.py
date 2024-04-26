from turtle import Turtle,Screen
import random
s1 = Screen()
t = Turtle()
t.shape("circle")
t.speed(10)
list_color  = ["red","purple","orange","brown","blue","alice blue","turquoise","lightgreen"]
for i in range(300) : 
    t.up()
    rand_forward = random.randint(10,130)
    t.forward(rand_forward)
    rand_angle = random.randint(0,360)
    t.dot(20,f"{random.choice(list_color)}")
    t.lt(rand_angle)
s1.exitonclick()