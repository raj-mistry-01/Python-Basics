from abstraction1 import Vehicle
class Bike(Vehicle) :
    def __init__(self,n) -> None:
        self.n = n
    def start(self) :
        print("You can start with kick.")
class Scooty(Vehicle) :
    def __init__(self,n) -> None:
        self.n = n
    def start(self) :
        print("Cell Start.")
class Car(Vehicle) :
    def __init__(self,n) -> None:
        self.n = n
    def start(self) :
        print("Start with key.")