# If Statement: Used to check the first condition.
# If it's True, the code inside it runs, and the rest is skipped.
age = 20
if (age >= 18):
    print("You can vote")

# elif(else if) Statement: Comes after if. Used to check another condition if the if condition was False.
# You can have multiple elif blocks.
light = "green"
if (light == "red"):
    print("Stop")
elif (light == "green"):
    print("Go")
elif (light == "Yellow"):
    print("Look")

# else statement: Comes at the end. Runs if none of the if or elif conditions are True.
# You can’t use a condition with else.
password = "admin123"

if password == "admin":
    print("Access granted.")
else:
    print("Access denied.")

# Indentation: Indentation means the spaces or tabs you put at the beginning of a line of code.
# The standard in Python is to use 4 spaces for indentation.
# In an if, elif, and else statement, parentheses() are optional.

# WAP to check if a number entered by the user is odd or even.
number = int(input(" Enter the number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

#WAP to find the greatest of 3 numbers entered by the user.
first_number = int(input("Enter the First number: "))
second_number = int(input("Enter the Second number: "))
third_number = int(input("Enter the Third number: "))
if first_number >= second_number and first_number >= third_number:
    print("The Greatest Number is:", first_number)
elif second_number >= first_number and second_number >= third_number:
    print("The greatest number is:", second_number)
else:
    print("The greatest Number is:", third_number)

# WAP to check if a number is a multiple of 7 or not.
a = int(input("Enter the number: "))
if a % 7 == 0:
    print("Multiple of 7")
else:
    print("Not a multiple")
