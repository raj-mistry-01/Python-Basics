# take a input from user and init by class.
Var = input("Enter a number : ")
class createVar :
    def __init__(self,Var) -> None:
        self.Var_=Var
obj=createVar(Var)
print(obj.Var_)