# Loops are used to repeat instructions.
# Two Types of Loops: While loop and For Loop.

# While Loop
i = 1
while i <= 5:
    print("Hello World", i)
    i += 1
# Print numbers form 1 to 20
i = 1
while i <= 20:
    print(i)
    i += 1

# Print numbers from 20 to 1
i = 20
while i >= 1:
    print(i)
    i -= 1

# Print the multiplication table of a number n.
i = 1
n = int(input("Enter the number:"))
while i <= 10:
    print(n * i)
    i += 1
# Print the elements of the following list using a loop.
# [1,4,9,16,25,36,49,64,81,100]
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 0
while idx < len(nums):
    print("Numbers of Index is:", nums[idx])
    idx += 1

# Break: Used to terminate the loop when encountered.
i = 1
while i <= 5:
    print(i)
    if i == 3:
        break
    i += 1
print("end of loop")

# Continue: Terminates execution in the current iteration & execution of the loop with the next iteration.
i = 0
while i <= 5:
    if i == 3:
        i += 1
        continue  # acts as skip
    print(i)
    i += 1

# For Loop: A for loop in Python is used to iterate over a sequence (like a list, tuple, string, or range)
# and execute a block of code for each element in that sequence.
nums = [10, 20, 25, 29, 5.5, "ABC"]
for value in nums:
    print("Value of list : ", value)

# search for a number x in this tuple using loop.
nums = (1, 4, 9, 16, 25, 36, 49, 64, 101)
x = 36
idx = 0
for value in nums:
    if value == x:
        print("Number found at idx", idx)
    idx += 1

# Range(): Range functions returns a sequence of numbers, starting from 0 by default,
# and increments by 1 (by default), and stop before a specified number.
# Eg: range (5):---> Start = 0, step(increments) = 1 and end = 5(ending no. is not included)
# When you pass only one number to range(5), it is treated as the stopping point,
# and counting starts from 0 by default.
# When you pass Two numbers to range(2,10), it is treated as Stat and Stop point.
# When you pass Three numbers to range(2,10,2), its is treated as Start, Stop and Step Size(increment by).
print("First loop with Stop condition")
for i in range(5):
    print(i)
print() # The print() function without any arguments is used to print an empty line in Python.

print("Second loop with Start and Stop condition")
for i in range(2,10):
    print(i)
print()

print("Third loop with Start, Stop and step size condition")
for i in range(2,10,2):
    print(i)
print()

# Print the multiplication table of a number n.
n = int(input("Enter the number:"))
for i in range(1,11):
    print(f"{n} x {i} = {n * i}")
#An f-string(Formatted string) is a way to create a string in Python that can include
# variables or expressions directly inside the string using curly braces {}.
