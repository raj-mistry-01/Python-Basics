# calculate the circumference and the area of the circle.
import math 
class circle :
    def __init__(self,radius) -> None:
        self.radius = radius
        self.area = math.pi * (radius**2)
        self.cfr = 2*math.pi*radius
    def show() :
        print(f"The area is {circle1.area} and circumference {circle1.circumference} . ")

circle1 = circle(12)
choice = input("Type 'Yes' :")
if choice == "Yes" :
    circle1.show()
