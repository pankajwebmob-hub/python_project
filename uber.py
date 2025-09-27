# class UberTPT:
#     company_name = "Uber"
#     numberplate_color = "Yellow"
#
# car = UberTPT()
# print("Car Company Name:",car.company_name)
# print("Car Numberplate color:", car.numberplate_color)


class UberTPT:
    company_name = "Uber"
    numberplate_color = "Yellow"

    def __init__(self,driver_name, car_model, reg_number,):
        self.driver_name = driver_name
        self.car_model = car_model
        self.reg_number = reg_number

    def display_details(self):
        print("Company Name:", UberTPT.company_name)
        print("Numberplate color:", UberTPT.numberplate_color)
        print("Driver Name:", self.driver_name)
        print("Car Model:", self.car_model)
        print("Registration Number:", self.reg_number)

car1 = UberTPT("Rohit", "XUV300", "HP89-4777")
car1.display_details()
car2 = UberTPT("Pamma", "Innova", "HR49-4444")
car2.display_details()
