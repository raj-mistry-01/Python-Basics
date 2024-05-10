# changing a method of a super class in Sub class  is called Overriding.
class human :
    def work(self) :
        print("I can Work.")
    
class Male(human) :
    def work(self):
        print("I can Code.")

male1 = Male() 
male1.work()

# what if we want to print super class methods from sub class.
# Use the function super() in the subclass.

class human :
    def work(self) :
        print("I can Work.")
    
class Male(human) :
    def work(self):
        super().work()
        print("I can Code.")

male1 = Male() 
male1.work()

