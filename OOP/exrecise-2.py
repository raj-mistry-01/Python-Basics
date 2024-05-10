# take a inout from a class and it print if by another class.
class input_ :
    def __init__(self) -> None:
        self.name = input("Enter your name :")
        self.age = input("Enter your age : ")

class print1(input_) :
    def print_(self) :
        print(obj.name)
        print(obj.age)

obj=print1()
obj.print_()