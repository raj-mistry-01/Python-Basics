# to learn abstaction prefer abstraction1,2,3 .py
# abstraction means which data should be shown to user and which should be hidden.
from abc import ABC , abstractmethod # abc mans abstractclass
class Vehicle :
    def __init__(self,n) -> None: # n = no.of tyres.
        self.n = n
    @abstractmethod
    def start(self) : # abstract Method.
        pass 
    def desplay(self) : # concrete Method or normal Method.
        print("Hey I am calling from abstract class.")
v = Vehicle(2)