# how mro works.
# mro() function works  for the class.
# mro() can be understiid by c3 linearization algorithem. 
# c3 algorithem :
# first from left to right then upper class.
# for any class it always look for the own class then heriting class(if any) and last is object class 
# so for any class least mro() will be <class "own class"> <class "Object">
class a :
    def show() :
        print("from class a")

class b(a) :
    def show():
        print("from class b")

class c(a) :
    def show():
        print("from class c")

class d(b,c) :
    pass

class e(c,b) :
    pass
print(d.mro())  # it is (b,c)
print(e.mro())  # it is (c,b)
