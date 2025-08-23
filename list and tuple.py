# lists: A list is a mutable, ordered collection of items. You can change,
# add, or remove items from a list after it is created.

fruits = ["apple", "mango", "cherry"]
print(fruits)

# Accessing elements
print(fruits[1])

# Modifying elements
fruits[0] = "Kivi"
print(fruits)

# Adding elements
fruits.append("Banana")
print(fruits)

# Inserting at a specific position.
fruits.insert(3,"Orange")
print(fruits)

# Removing elements
fruits.remove("Banana")
print(fruits)

# Popping (removing by index)
fruits.pop(1)
print(fruits)

# Length of list
print(len(fruits))

# Tuples: A tuple is an immutable, ordered collection of items.
# Once created, you cannot change its elements (i.e., no append, remove, or item assignment).

my_tuple = (1,2,3, "Hello")
print(my_tuple)
# For a single-element tuple, use a comma: (5,)
a = (15,)
print(a)

# creating a tuple
emp_data = ("Varun Sood", 35, "BCM", 9122344455,"Shimla")
print(emp_data)

# Accessing elements
print(emp_data[0])

# Slicing
print(emp_data[1:])
# If you perform slicing and do not define the end index, then Python will print all the elements
# from the starting index to the end of the list or tuple.

# Length of tuple
print(len(emp_data))



