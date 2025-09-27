class Car:
    def start(self):
        print("Car Started...")

    def stop(self):
        print("Car Stopped.")

class TataCar(Car):
    def __init__(self, brand):
        self.brand = brand

class Nexon(TataCar):
    def __init__(self, brand, type):
        super().__init__(brand) # This calls the constructor of the parent class (TataCar).
        self.type = type

car1 = Nexon("Tata","Petrol")
print(car1.brand)
print(car1.type)
car1.start()
