# encapsulation is also known as data hiding.
# the best methods to encapsulate the data is --
# getter and setter method.
# using get and set method , it is easy to modify private attributes.
class student :
    def __init__(self,name) -> None:
        self.__name = name
    def get_name(self) :
        return self.__name
    def set_name(self,name) :
        if len(name) > 40 :
            print("You entered more than limit.")
        else :
            self.__name = name

obj = student("Raj")
print(obj.get_name())
obj.set_name("Minali")
print(obj.get_name()) 