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
print("The sum of", a, "and", b, "is: ", total)
diff = a - b
print("The difference of", a, "and", b, " is: ", diff)
product = a * b
print("The product of", a, "and", b, "is: ", product)
quotient = a//b
print("The quotient of", a, "and", b, "is: ", quotient)
remainder = a%b
print("The remainder of", a, "divided by", b, "is: ", remainder)
log10a = math.log(a, 10)
print("The base 10 log of", a,  "is: ", log10a)
power = a ** b
print(a, "raised to the power of", b, "is: ", power)