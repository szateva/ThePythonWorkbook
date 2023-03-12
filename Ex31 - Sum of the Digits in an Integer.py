"""
Develop a program that reads a four-digit integer from the user and displays the sum of the digits in the number.
For example, if the user enters 3141 then your program should display 3+1+4+1=9
"""

num_str = input("Please type in a 4-digit number: ")

total = int(num_str[0]) + int(num_str[1]) + int(num_str[2]) + int(num_str[3])
concatenated = "+".join(num_str)        #join takes a variable that is iterable

print(concatenated, "=", total)