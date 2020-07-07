"""
before compiling this program u have to clear all the bookish part.After clearing the all doubts
u can complie th
"""



class Vehicle:
    """Base class for all vehicles"""

    def __init__(self, name, manufacturer, color):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color

    def drive(self):
        print(f"Driving {self.manufacturer} {self.name}")
    def turn(self, direction):
        print(f"Turning {self.name} to {direction}")

    def brake(self):
        print(f"{self.name} is stopping")


class Car(Vehicle):
    """Car Class"""
    def __int__(self, name, manufacturer, color, year):
        print("Creating A Car")
        super().__init__(name, manufacturer, color)
        print(f"A new Car has been created. name: {self.name}")
        print(f"It has {self.wheels} wheels")
        print(f"This Car Was Built in {self.year}")

    def change_gear(self, gear_name):
        """Method Of Changing gear"""
        print(f"{self.name} is changing gear to {gear_name}")
    def turn(self, direction):
        print(f"Turning {self.name} to {direction}")

class Motorcycle(Vehicle):
    """MotorCycle Class"""
    def __init__(self, name, manufacturer, color):
        print("Creating a Motor Cycle")
        super(Motorcycle, self).__init__(name, manufacturer, color)
        self.year = 2017
        self.color = "red"
        print(f"The Motorcycle's Name:{self.name}\n Manufacturer:{self.manufacturer}\n Color: {self.color}")
if __name__ == "__main__":
    """
    v1 = Vehicle("Fusion 110 Ex", "Walton", "Black")
    v2 = Vehicle("Softtail Delux", "Harley-Davidson", "Blue")
    v3 = Vehicle("Mustanf 5.0 GT Coupe", "Ford", "Red")

    v2.drive()
    v3.drive()
    v1.turn("left")
    v2.turn("right")

    v1.brake()
    v2.brake()
    v3.brake()
    """

    z = Motorcycle("Shagato", "Shagato 1", "Shagato 2")
