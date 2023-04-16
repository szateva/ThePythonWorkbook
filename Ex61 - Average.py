""" In this exercise you will create a program that computes the average of a collection of values entered by the user.
The user will enter 0 as a sentinel value to indicate that no further values will be provided. Your program should display
your program should display an appropriate error message if the first value entered by the user is 0. """

counter = 0
total = 0
average = 0

print("Please, enter the numbers you want to average. Enter 0 to stop.")

value = int(input("Please, enter a value: "))
if value == 0:
    print("You haven't entered any values.")
else:
    while value != 0:
        total += value
        counter += 1
        value = int(input("Please, enter a value: "))
    average = total / counter
    print(f"The average of the values you entered is {average}.")
