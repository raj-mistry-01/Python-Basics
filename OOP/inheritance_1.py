# accesing the attributes of the super class.
# yoiu have to super function with init function.
class employee :
    def __init__(self,name) -> None:
        self.name = name

class emp1(employee) :
    def __init__(self,name) -> None:
        super().__init__(name)

emp_1 = employee("Raj")
print(emp_1.name)