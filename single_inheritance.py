# Single Inheritance:
class Car:
    def start(self):
        print("Car Started...")

    def stop(self):
        print("Car Stopped.")

class TataCar(Car):
    def __init__(self, name):
        self.name = name

car1 = TataCar("Nexon")
car2 = TataCar("Safari")

print(car1.name)
car1.start()
car1.stop()

print(car2.name)
car2.start()
car2.stop()