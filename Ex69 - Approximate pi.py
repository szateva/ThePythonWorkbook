"""The value of pi can be approximated by the following infinite series:
pi = 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - 4/(8*9*10) + 4/(10*11*12) - ...
Write a program that displays 15 approximations of pi. The first approximation should make use of only the first term
from the infinite series. Each additional approximation displayed by your program should include one more term in the
series, making it a better approximation of pi than any of the approximations displayed previously."""

pi = 3
numerator = 4
denominator = 2

print(f"Approximation 0 of pi is {pi:.15f}")

for i in range(1, 16):
    pi += numerator / (denominator * (denominator + 1) * (denominator + 2))
    numerator *= -1
    denominator += 2
    print(f"Approximation {i} of pi is {pi:.15f}")
