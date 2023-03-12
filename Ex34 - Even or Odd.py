"""
Write a program that reads an integer from the user. Then your program should display a message indicating whether
the integer is even or odd.
"""

num = int(input("Please, type a number: "))

if num % 2 == 0:
    print(num, "is even.")

else:
    print(num, "is odd.")