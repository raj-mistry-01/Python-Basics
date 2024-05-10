# MRO in multiple Inheritance.
# Method 

class class1:
    def __init__(self) -> None:
        self.name = "Raj"
    def work(sef) :
        print("From Super 1.")

class class2 :
    def __init__(self) -> None:
        self.age = 12
    def work(self) :
        print("From super 2.")

class sub1(class1,class2) :
    pass 

obj1 = sub1()
print(obj1.work()) # will work for the class1

# first write class2
class sub2(class2,class1) :
    pass 

obj1 = sub2()
print(obj1.work()) # will work for the class2

# So on which class will be priorer if the methods are same written.
# So the first passing class will be considered.
# To know that order mro() function is used.
# mro() function is used on a derived class.
# mro() stands for Method Resolution Order. 
print(sub1.mro())

# multiple attributes.
obj2 = sub2()
print(obj2.age)
# what if I want name in obj2 also ??
# but sub2 will only have age attribute and mro is first class2 than 1.

