"""Implement the Euclid's algorithm (greatest common divisor). """

m = int(input("Please enter a positive integer: "))
n = int(input("Please,enter another positive integer: "))

d = min(m,n)

while (n % d != 0) or (m % d != 0):
    d -= 1
print(f"The greatest common divisor of {m} and {n} is {d}")