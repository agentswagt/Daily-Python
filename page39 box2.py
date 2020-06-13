class Car:
    def __init__(self, n, c): #__init__ eta ke constructor bole
        self.name = n
        self.color = c
    def start(self):
        print(f"Name: {self.name}, Color: {self.color}")
        print("Starting the engine")
my_car1 = Car("Formula", "Black")
my_car1.start()
my_car2 = Car("Roddur", "Roy")
my_car2.start()
my_car3 = Car("Hacker", "Rank")
my_car3.start()