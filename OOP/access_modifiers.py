# for data hiding and showing purpose there are access_modifiers.
"""
1) Public
2) Protected
3) Private
"""
"""
like if we have a class , have some attributes and method 
What are limitations to access it .
how to put that limited access to other, that are the access_modifiers.
if class can be used by anyone then  it is public.
if we want that only some authorised members(inherited class other) should use that then we have to apply protected .
if only owner cna use it , then apply private modifier.(within that class only it's attributes and methodes can be used.)
"""
class student :
    def __init__(self,name,rn) -> None:
        self.name = name # public instance object.
        self._rollNo = rn # use _ (underscore) to make a protected instance object.
    def display(self) :
        print(f"Student name is {self.name} , Roll Number is {self._rollNo}.")

class objectCreator (student) :
    pass

obj1 = objectCreator("Raj",12)
obj1.display() # can be accesed outside the class.
# even protected is accessed by the outside code.
# so for me