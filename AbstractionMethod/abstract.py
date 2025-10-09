from abc import ABC,abstractmethod

class Vehical(ABC):
    @abstractmethod
    def start(self):
        pass
    
class Car(Vehical):
    def start(self):
        print("Car engine started...")

class Ebike(Vehical):
    def start(self):
        print("E-Bike dos't have engin..")
        
class Bike(Vehical):
    
    def start(self):
        print("Bike is started...")

for v in [Car(),Ebike(),Bike()]:
    v.start()
    