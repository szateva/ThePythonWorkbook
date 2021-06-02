""" read two integers a and b from user
 compute and display:
 sum of a and b
 difference a - b
 quotient a/b
 remainder of a/b
 log base 10 of a
 a^b"""
import math

a = int(input("Type an integer: "))
b = int(input("Type another integer: "))

total = a + b
print("The sum is: ", total)
diff = a - b
print("The difference is: ", diff)
product = a * b
print("The product is: ", product)
quotient = a//b
print("The quotient is: ", quotient)
remainder = a%b
print("The remainder is: ", remainder)
log10b = math.log(b, 10)
print("The base 10 log of b is: ", log10b)
power = a ** b
print("a raised to the power of b is: ", power)