"""
A univariate quadratic function has the form f(x) = ax^2 + bx + c, where a, b and c are constants, and a is non-zero.
The roots of a quadratic function can be found by finding values of x that satisfy the quadratic equation
ax^2 + bx + c = 0. A quadratic equation may have 0, 1 or 2 real roots. These roots can be computed using the quadratic
formula, shown below:
        root = (-b+- sqrt(b^2 - 4ac))/(2a)

The portion of the expression under the square root sign is called the discriminant. If the discriminant is negative
then the quadratic equation does not have any real roots. If the discriminant is 0, then the equation has one real
root. Otherwise, the equation has two real roots, and the expression must be evaluated twice, oce using a plus sign, and
once using the minus sign, when computing the numerator.
Write a program that computes the real roots of a quadratic function. Your program should begin by prompting the user
for the values of a, b and c. Then it should display a message indicating the number of real roots, along with the
values of those real roots (if any).
"""

import math

print("You can find the roots of a quadratic equation if you specify the coefficients a, b and c in the generic form:")
print("ax^2 + bx + c")
print("where a is the quadratic coefficient, b is the linear coefficient and c is the constant coefficient.")
a = float(input("Please, enter the quadratic coefficient, a = "))
b = float(input("Please, enter the linear coefficient, b = "))
c = float(input("Please, enter the constant coefficient, c = "))

discriminant = b**2 - 4*a*c

if discriminant < 0:
    print(f"Sorry, the quadratic equation {a}x^2 + {b}x + {c} has no real roots.")
elif discriminant == 0:
    root = (-b)/(2*a)
    print(f"The quadratic equation {a}x^2 + {b}x + {c} has one real root: {round(root, 2)}.")
else:
    root1 = ((-b) + math.sqrt(discriminant))/(2*a)
    root2 = ((-b) - math.sqrt(discriminant))/(2*a)
    print(f"The quadratic equation {a}x^2 + {b}x + {c} has two real root: {round(root1, 2)} and {round(root2, 2)}.")