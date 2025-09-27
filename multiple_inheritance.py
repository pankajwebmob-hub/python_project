class Engine:
    def engine_info(self):
        print("This is a powerful engine.")

class Wheels:
    def wheels_info(self):
        print("This car has 4 wheels.")

class Car(Engine, Wheels):
    def car_info(self):
        print("This is a sports car.")

# Create object
my_car = Car()

# Access methods from both parent classes
my_car.engine_info()
my_car.wheels_info()
my_car.car_info()
