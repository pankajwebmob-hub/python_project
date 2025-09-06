# Encapsulation is the practice of hiding the internal state of an object and requiring
# all interaction to be performed through an object’s methods.
class Student:
    def __init__(self):
        self.__name = "John"  # Private variable

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

s = Student()
print(s.get_name())   # Accessing private variable using getter
s.set_name("Alice")   # Modifying using setter
print(s.get_name())
print("-------")
# self.__name → A private variable (by convention, double underscore makes it private).
# get_name() → Getter method to access the name.
# set_name() → Setter method to change the name.
# s = Student() → Creates a Student object.
# print(s.get_name()) → Accesses the private name safely.
# s.set_name("Alice") → Updates the private variable.

# Inheritance allows one class (child) to use properties and methods of another class (parent).
# class Animal:
#     def speak(self):
#         print("Animal speaks")
#
# class Dog(Animal):  # Inherits from Animal
#     def bark(self):
#         print("Dog barks")
#
# d = Dog()
# d.speak()   # Inherited method
# d.bark()    # Own method
# print("-------")
# class Dog(Animal): → Dog inherits from Animal.
# d.speak() → Uses Animal’s method.
# d.bark() → Uses its own method.

# Polymorphism means many forms. In OOP, it allows different classes to
# implement the same method in different ways.
# class Cat:
#     def sound(self):
#         print("Meow")
#
# class Dog:
#     def sound(self):
#         print("Bark")
#
# for animal in (Cat(), Dog()):
#     animal.sound()
# print("------")
# Cat and Dog both have a method called sound(), but the behavior is different.
# for animal in (Cat(), Dog()): → Loop through both objects.
# animal.sound() → Calls the appropriate method for each object.

# Abstraction means hiding complex implementation details and showing only essential features.
# In Python, you use the abc module for this.
# from abc import ABC, abstractmethod
#
# class Vehicle(ABC):  # Abstract base class
#     @abstractmethod
#     def start_engine(self):
#         pass
#
# class Car(Vehicle):
#     def start_engine(self):
#         print("Car engine started")
#
# c = Car()
# c.start_engine()
# from abc import ABC, abstractmethod → Used to define abstract classes.
# class Vehicle(ABC): → Abstract base class.
# @abstractmethod → Marks the method that must be implemented by any subclass.
# class Car(Vehicle): → Subclass that implements the abstract method.
# c.start_engine() → Calls the concrete implementation.

class Dog:
    def __init__(self, name):
        self._name = name  # protected

dog = Dog("Tommy")
print(dog._name)  # ⚠️ Accessible, but not recommended
