"""
Create a program that reads three integers from the user and displays them in sorted order (from smallest to largest).
Use the min and max functions to find the smallest and largest values. The middle value can be found by computing the
sum of all three values, and then subtracting the minimum and maximum values.
"""

num1 = int(input("Please type a number: "))
num2 = int(input("Please type a second number: "))
num3 = int(input("Please type a third number: "))

total = num1 + num2 + num3
middle_no = total - min(num1, num2, num3) - max(num1, num2, num3)

print("The numbers in ascending order are: ", min(num1, num2, num3), middle_no, max(num1, num2, num3))