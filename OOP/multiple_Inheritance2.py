# seting a attribute of an object from sub class .
class sup1 :
    def __init__(self,name) -> None:
        self.name = name

class sup2 :
    def __init__(self,age) -> None:
        self.age = age

class sub(sup1,sup2) :
    def __init__(self,name,age) -> None: # have to make init for sub class and define another init funcitons for super class which are herited to the subclass.
        sup1.__init__(self,name)
        sup2.__init__(self,age)

obj = sub("Raj",12) #  To want age from sup2 and name from sup1 We need to call both init funciton from the class within it's init function.
print(obj.age)
print(obj.name)