"""Print the prime factors of a number entered by the user."""

"""The prime factorization of an integer, n, can be determined using the following steps:

Initialize factor to two
While factor is less than or equal to n do
    If n is evenly divisible by factor then
        Conclude that factor is a factor of n
        Divide n by factor using integer division
    Else
        Increase factor by one

Write a program that reads an integer from the user. If the value entered by the user is less than 2 then your program
should display an appropriate error message. Otherwise your program should display the prime numbers that can be
multiplied together to compute n, with one factor appearing on each line. For example:
Enter an integer (2 or greater): 72
The prime factors of 72 are:
2
2
2
3
3
"""

n = int(input("Please, enter an integer (2 or greater): "))

factor = 2
if n < 2:
    print("Sorry, the integer you entered is less than 2.")
else:
    print(f"The prime factors of {n} are:")
    while factor <= n:
        if n % factor == 0:
            print(f"{factor}")
            n = n // factor
        else:
            factor += 1