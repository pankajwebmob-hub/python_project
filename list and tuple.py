# lists: A list is a mutable, ordered collection of items. You can change,
# add, or remove items from a list after it is created.

# fruits = ["apple", "mango", "cherry"]
# print(fruits)
#
# # Accessing elements
# print(fruits[1])
#
# # Modifying elements
# fruits[0] = "Kivi"
# print(fruits)
#
# # Adding elements
# fruits.append("Banana")
# print(fruits)
#
# # Inserting at a specific position.
# fruits.insert(3,"Orange")
# print(fruits)
#
# # Removing elements
# fruits.remove("Banana")
# print(fruits)
#
# # Popping (removing by index)
# fruits.pop(1)
# print(fruits)
#
# # Length of list
# print(len(fruits))
#
# # Tuples: A tuple is an immutable, ordered collection of items.
# # Once created, you cannot change its elements (i.e., no append, remove, or item assignment).
#
# my_tuple = (1,2,3, "Hello")
# print(my_tuple)
# # For a single-element tuple, use a comma: (5,)
# a = (15,)
# print(a)
#
# # creating a tuple
# emp_data = ("Varun Sood", 35, "BCM", 9122344455,"Shimla")
# print(emp_data)
#
# # Accessing elements
# print(emp_data[0])
#
# # Slicing
# print(emp_data[1:])
# # If you perform slicing and do not define the end index, then Python will print all the elements
# # from the starting index to the end of the list or tuple.
#
# # Length of tuple
# print(len(emp_data))
# print("--------")

# Create a fruit list with Dynamic Version:
fruits = []

# Asking for input directly
fruit1 = input("Enter fruit 1: ")
fruit2 = input("Enter fruit 2: ")
fruit3 = input("Enter fruit 3: ")

# Adding fruits to the list
fruits.append(fruit1)
fruits.append(fruit2)
fruits.append(fruit3)

print("Fruits List:", fruits)
print("---------")

# Create a Fruit list with Loop:
fruits = []

# Ask user how many fruits they want to add
num_fruits = int(input("How many fruits would you like to add? "))

# Loop to add fruits
for i in range(num_fruits):
    fruit = input(f"Enter fruit {i+1}: ")
    fruits.append(fruit)

print("Fruits List:", fruits)


