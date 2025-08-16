Name = "Manish"
Department = "Commercial"
Age = 35
Salary = 50000.500
# print("My Name is:", Name)
# print("My Department is:", Department)
# print("My Age is:", Age)

print(f"My name is:{Name} \nMy Department is: {Department} \nMy Age is: {Age}")
# f"..." is called an f-string, which allows variables to be directly embedded inside a string.

print(type(Name))
print(type(Age))
print(type(Salary))

# Arithmetic Operators
x = 20
y = 6
Sum = x + y
diff = x - y
mul = x * y
div = x / y
mod = x % y
print(Sum)
print(diff)
print(mul)
print(round(div, 2))
print(mod)

# Relational Operators
# A relational operator will always return either True or False as output, which is a Boolean value.
a = 22
b = 37
print(a == b)
print(a != b)
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)

# Assignment Operators
num = 30
num = num+50
# We can also write it as num += 50
mul = 5
mul *=6
print("The value of num is:", num)
print("The value of multiplication is:",mul)

# Logical Operator(Not, And, Or)
a = 15
b = 12
print(not (a>b))
print(not (a<b))

x = True
y = False
print("Value of And Operator is:", x and y )
print("value of Or operator is:", x or y)

# Input() statement is used to accept values (using keyboard) from user.
# input() in Python always returns a string.
name = input(" Enter your Name: ")
print("My Name is:", name)

# Write a program to input 2 numbers & print their sum
# int(input(...)) converts the input from string to integer.
First_Value = int(input("Enter First value:"))
Second_Value = int(input("Enter Second value"))
sum = First_Value+Second_Value
print("Total sum of two values are:",sum)

# Write a program to input 2 int numbers a and b. Print True if a is greater than b. If not print False

a = int(input(" Enter the first no:"))
b = int(input("Enter the second no"))
# print(a>b)
if a > b:
    print(True)
else:print(False)

