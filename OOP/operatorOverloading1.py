# the power of operatorOverloading
# using + as greater than operator.
class sup:
    def __init__(self,num) -> None:
        self.num = num

class gt(sup) :
    def __init__(self,num) -> None:
        sup.__init__(self,num)
    def __add__(self,other) :
        if self.num > other.num :
            return print(f"{self.num} is > {other.num}.")
        else : 
            return print(f"{other.num} is > {self.num}.")


p = gt(4)
q = gt(7)
print(p+q) # see the O/p