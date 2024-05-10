# Multiple heritance means deriving 2 or more super class to the sub class.
class sup1 :
    def main(self) :
        print("Hey , I am from super 1.")
    
class sup2 :
    def main2(self) :
        print("Hey , I am from super 2.")

class sub(sup1,sup2) :
    pass

obj1 = sub()
obj1.main()
obj1.main2()