from turtle import Turtle,Screen
import random
list_color  = ["red","purple","orange","brown","blue","alice blue","turquoise","lightgreen"]
s1 = Screen()
t = Turtle()
t.speed(120)
for i in range(120) :
    t.pencolor(random.choice(list_color))
    t.circle(100)
    t.lt(3)
s1.mainloop()
# for color you can also write that --
"""
r = radnom.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)
"""
