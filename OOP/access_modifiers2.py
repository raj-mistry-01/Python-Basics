# accessing private attribute from outside 
# name mangling method.
class super :
    def __init__(self,name) -> None:
        self.__name = name
    def __display(self) :
        print(f"My name is {self.__name}.")

s1 = super("Raj")
print(s1._super__display())