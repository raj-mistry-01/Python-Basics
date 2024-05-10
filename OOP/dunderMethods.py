# methods with __ double underscore at starting and ending both.
# they are called implicitely.
# ther power of the dunder method is that we can define inbuilt functions by own 
# some useful dunder methos --
"""
__str__
__len__
__call__
__add__
... many more
"""

class c1 : 
    def __init__(self,name,age) -> None:
         self.name = name
         self.age = age

obj1 = c1("Raj",17)
print(obj1) # not desired output , we want that name and age should be printed.

# when we pront an obj str method is called.

# solution of the above.
class c2(c1) :
     def __init__(self, name, age) -> None:
          super().__init__(name, age)
     def __str__(self) -> str:
          return f"{self.name} & {self.age}"

obj2 = c2("Raj",17)
print(obj2) # see the output.