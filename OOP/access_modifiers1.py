# private access
# limited to only super class access.
class super :
    def __init__(self,name) -> None:
        self.__name = name # use double underscore to make private attribute.
    def __display(self) : # private method.
        print(f"My name is {self.__name}.")
    def display(self) :
        self.__display() # making a function to access private method , should ne in class.
# class sub1 (super) :
#     pass

# obj1 = sub1()
# obj1.__display() # will lead to an error , because super class has own private method and attribute so it's inherited class can not access it.

# obj1 = super() 
# obj1.__display() even this will lead to an error. you can not acces private method outside the class.
    
obj1 = super("Raj")
obj1.display() # solution of the above.