class main :
    def __init__(self) -> None:
        self.name = input("Enter a name : ")

class sub1 (main) :
    def print_ (self) :
        print(obj.name)
obj = sub1()
obj.print_()
print(sub1.mro())