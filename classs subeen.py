class Car:
    driver = ""
    color = ""
    def start(self):
        print("Starting Engine")
#creating Car objects
my_car = Car()
#giveing atribute to my_car
my_car.driver = "Subeen"
my_car.color = "White"

print(f"The name of driver is {my_car.driver}, and the color of this car is {my_car.color}")
my_car.start()