print(1+2)
print("1" + "2")
# dunder methods ---------
"""
starts and ends with __ (double underscore).
"""
# when we write + what is the behind the scenes.
# __add__ is called . 
# it is dunder method.
print(int.__add__(1,2))
print(str.__add__("1","2"))

# redifing a dunder we can do below like ---
class comp :
    def __init__(self,real,imaginary) -> None:
        self.real = real
        self.imaginary = imaginary
    def __add__(self,other) :
        p = self.real + other.real
        q = self.imaginary + other.imaginary
        print(f"{p}+{q}j.")

c1 = comp(1,2)
c2 = comp(1,2)
print(c1+c2)
# above code defines that giving own method or behaviour to + operator.