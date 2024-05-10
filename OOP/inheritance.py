"""
inheritance means passing one class's elements (attributes and methodes) to other class.
"""
# syntax -- 
# class childClass (parentClass) :
#  -- class statements.

# Why Inheritance -- 

class human :
    def eat(self) :
        print("I can eat")
    def work(self) :
        print("I can work.")

class male(human) :
    def speak(self) : # own method of sub class.
        print("I can speak.")

# rather than writing :
""""
class male() :
    def eat(self) :
        print("I can eat")
    def work(self) :
        print("I can work.")
"""
# male is also human SO we have just passed the class Human to the make class and NOw male class can access all method and attribute of the human class.
# this is the advantage of teh Inheritance  , Reduces the code length.
male1= male()
male1.eat()
male1.speak(male1)