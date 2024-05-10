# A very important way to create an object.
# using constructor method.
# What if we want we have to just intialize the attribute nnot to give value.
# That time self and __init__ function is used.
# __init__ function is  a special function with predefined parameter self.
# these function automatically invokes when we create an object.
# self parameter passes on which __init__ function is working on.
class constructor :
    def __init__(self,name,address) -> None:
        self.name_=name
        self.address_=address

object_1 = constructor("Raj","Mehmedabad")
print(f"The name of the object is {object_1.name_}.")
object_2  = constructor("Parth","Ahemadabad")
print(f"The address of the object is {object_2.address_}.")