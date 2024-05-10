class sup :
    def comp_(self) :
        print("My Company is Hexane .")

class sub1(sup) :
    def emp(self) :
        print("I am an employee.")

class sub2(sub1) :
    def salary(self) :
        print("My salary is 1M $.")

obj = sub2(1)
print(obj.name)
obj1 = sub1()
obj.comp_()
obj.emp()
obj.salary()
obj1.comp_()
obj1.emp()
# obj1.salary() will lead to an error.