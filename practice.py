# # 1: Create a Simple Car Class
# class Car:
#     def __init__(self, brand, model):
#      self.brand = brand
#      self.model = model
#
#     def start(self):
#         print(f"The {self.brand} {self.model} is starting.")
# my_car = Car("Toyota", "Innova")
# my_car.start()

# class Person:
#     def say_Hello(self, name, age):
#         self.name = name
#         self.age = age
#         print(f"Hello, my name is {self.name} and I am {self.age} years old")
#
#
# p1 = Person()
# p1.say_Hello("Jack","30")

# class Laptop:
#     def __init__(self, brand, price):
#         self.brand = brand
#         self.price = price
#
#     def display(self):
#         print(f"Brand: {self.brand}, Price: {self.price}")
#
# l1 = Laptop("Dell",60000)
# l1.display()
# l2 = Laptop("Lenovo",70000)
# l2.display()

# class Circle:
#     def area(self,radius):
#         self.radius = radius
#         return (3.14 * radius * radius)
#
# c1 = Circle()
# print("Area of the Circle is:",c1.area(5))

class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive. ")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
        else:
            print(" Not enough balance or invalid amount.")

    def get_balance(self):
        return self.__balance

# Create an object of BankAccount
account = BankAccount()

# Deposit 100
account.deposit(100)

# Print balance
print("Balance:", account.get_balance())  # Should print 100

# Withdraw 30
account.withdraw(30)

# Print balance
print("Balance:", account.get_balance())  # Should print 70

# Try to withdraw too much
account.withdraw(100)  # Should print error message

# Print balance again
print("Balance:", account.get_balance())  # Should still print 70

