# Function: A function is a block of code that performs a specific task.
# It helps you organize your code and reuse logic easily.
def cal_sum(a, b):  # 'a' and 'b' are parameters; 'cal_sum' is the function name.
    sum = a + b
    print(sum)  # Displays the result on the screen.
    return sum  # Returns the result to wherever the function is called.


# 1.When you only define the function like above:
# You are just defining the function. You're telling Python:
# "If someone calls this function, this is what it should do."
# But since the function is not being called, the code inside it doesn't run.
# That’s why no output is shown.

# 2.When you call the function like this:
cal_sum(6, 10)  # Function call; 6 and 10 is called arguments.


# This calls the cal_sum function with arguments 6 and 10.
# The function runs, prints 16, and returns 16
# Now you're saying: "Run this function using 6 and 10 as inputs."
# So the function runs:
# 1. sum = 6 + 10 → sum = 16
# 2. print(sum) → prints 16
# 3. return sum → returns 16 (can be used later)
# 4. That’s why you now see 16 in the output.

# Find the average of 3 numbers
def cal_avg(x, y, z):
    avg = (x + y + z) / 3
    print(avg)
    return avg


cal_avg(1, 2, 3)

# WAF to print the length of a list. (list is the parameter)
Trade_log = ["Date/Time", "Status", "Lender", "Borrower", "Currency", "Amount", "Rate", "Term"]
def print_len(data_list):
    print(len(data_list))
print_len(Trade_log)

# WAF to convert USD to INR
# Step1: Define the function
def converter(usd_val):
        inr_val = usd_val * 87
        print(usd_val,"USD =", inr_val, "INR")

# Step2: Call the function.
converter(1)

# WAF that takes a number as input and returns the string "Odd" if the number is odd,
# and "Even" if the number is even.
def check_odd_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Get input from the user
user_input = int(input("Enter a number: "))

# Call the function and store the result
result = check_odd_even(user_input)

# Print the result
print("The number is", result)
print() # This print() is used to add a blank line (space) between two outputs.


# Recursion: When a function calls itself repeatedly.
def show(n):
    if n == 0: # Base case
        return
    print(n)
    show(n-1)
show(5)

# Base case: A base case is the condition in a recursive function that stops
# the function from calling itself further.
# It acts as the exit point or stopping condition for recursion.