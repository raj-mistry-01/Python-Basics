# deriving more than one child from one parent.
# so derived (child) class can not access ant other chils class.
class sup :
    def out(self) :
        print('Hello World.!1')

class sub1(sup) :
    def out1(self) :
        print("Hello World!")

class sub2(sup) :
    def out2(self) :
        print("Hey I am from  2 .")

obj = sub1()
obj.out()
# obj.out2() will lead an error.