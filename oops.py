# Object-Oriented Programming (OOP) is a programming style that allows you to organize your code using:
# Classes (blueprints for creating objects)
# Objects (instances of classes)
# Methods (functions inside classes)
# Attributes (variables inside classes)

class Student:  # Class names in Python usually start with a capital letter.
    name = "Varun" # Class attribute named 'name' with default value "Varun"
    age = 30
    city = "PKL"
# An attribute is a variable that belongs to a class or an object.
# It stores data/information about the object.
# Example: A Student has attributes like: name, age, city


# Creates an object 's1' of the Student class; now 's1' can access class attributes and methods.
s1 = Student()
# Accesses the 'name' attribute of the 's1' object and prints it with a label.

print("Student name:",s1.name)
print("Student Age:",s1.age)
print("Student City:", s1.city)
print() # Prints an empty line; often used to improve readability of output.


class Car:
    brand = "Mahindra"
    model = "XUV3OO"
    color = "Silver"

car1 = Car()
print("Car Brand:",car1.brand)
print("Car Model:",car1.model)
print("Car Color",car1.color)
print()

# WAP to create a Bid request.
class Bid:
    amount = 0
    rate = 0

# Create an object of the class
bid1 = Bid()

# Take user input and assign to object attributes
bid1.amount = int(input("Enter the Amount: "))
bid1.rate = int(input("Enter the Rate: "))

# Validate and print result
if bid1.amount > 0 and bid1.rate >= 0:
    print("\u2705 Bid created successfully")
else:
    print("\u274C Error: Enter the valid Amount")
print("-------")

# init() Function:is a special method in Python that is automatically called when you create an object from a class.
# It is also called:The constructor of the class.
# It is used to initialize (set) values to object attributes when the object is created.

class Student:
    def __init__(self, name, marks):
        # This is the constructor method. It runs automatically when a new object is created.
        # 'name' and 'marks' are input parameters
        # 'self' refers to the current object being created

        self.name = name
        # Assign the value of 'name' to the object's 'name' attribute
        # Example: if name = "Rohit", then self.name = "Rohit"

        self.marks = marks
        # Assign the value of 'marks' to the object's 'marks' attribute
        # Example: if marks = 95, then self.marks = 95

        print("Adding new student details")
        # This line will print a message every time a student object is created

s1 = Student("Rohit", 95)
# Create an object 's1' of class 'Student' with name = "Rohit" and marks = 95
# This will call the __init__ method and print the message

print(s1.name, s1.marks)
# This prints the name and marks stored in object s1

s2 = Student("Vikram", 82)
# Create another object 's2' with name = "Vikram" and marks = 82
# Again, __init__ runs and prints the message

print(s2.name, s2.marks)
# Prints name and marks from object s2



