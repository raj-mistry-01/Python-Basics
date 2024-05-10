# method mean behaviour of an object .
# In simple terms method mean function of the class.
# methods will be for the obejct of the class.
# calling the method syntax --
#  objectName.functionName()
class constructor:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
    def display(self) :
        print(object1.name)

object1=constructor("Raj",17)
choice = input("Type 'Yes' :")
if choice == "Yes" :
    object1.display()

# another example -- 
class constructor:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
    def display(self,course) :
        print(f"The name is {self.name} and age is {self.age} , And he is learning {course}.") # object.course will lead to an error because there is no predifine attibute .

object2 = constructor ("Raj",17)
choice = input("Type 'Yes' :")
if choice == "Yes" :
    object2.display("C++")