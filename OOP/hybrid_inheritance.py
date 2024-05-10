# combination of more than one inheritance.
class a :
    def display(self) :
        print("from class a")

class b (a):
    def display(self) : 
        print("from class b")

class c :
    def show(self) :
        print("from class c")
    
class d(b,c) : # mulitple inheritance for d , b has a single inheritance so now d has hybrid inheritance.
    def show(self) :
        print("from class d")

dobj = d()
print(d.mro()) # mro goes to first child , child to super class
dobj.display() # it will be from be
dobj.show() # it will be from d

"""
if d (c,b) is there then mro will be changed .
"""