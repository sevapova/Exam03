'''12. Abstract Base Class
Task: Vehicle abstract classini yarating.'''


from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def info(self):
        pass


class Car(Vehicle):
    def info(self):
        return "Car engine started"


class Bike(Vehicle):
    def info(self):
        return "Bike engine started"


car = Car()
bike = Bike()

print(car.info())
print(bike.info())
