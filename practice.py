num = int(input("Enter the number:"))
if num == 0:
    print("Zero")
elif num % 2 == 0 and num > 0:
    print("Positive Even")
elif num % 2 != 0 and num > 0:
    print("Positive Odd")
elif num % 2 == 0 and num < 0:
    print("Negative Even")
# elif num % 2 != 0 and num <0:
#     print(" Negative Odd")
else:
    print("Negative Odd")







