"""
A bakery sells loaves of bread for $3.49 each. Day old bread is discounted by 60%. Write a program that begins by
reading the number of loaves of day-old bread being purchased by the user. Then your program should the regular
price for the bread, the discount because it is a day old, and the total price. All of the values should be displayed
using two decimal places, and the decimal points in all of the numbers should be aligned when reasonable values are
entered by the user.
"""
price_of_bread = 3.49
discounting_factor = 0.6

no_of_bread = int(input("How many day old bread have you purchased? "))

full_price = round(no_of_bread*price_of_bread, 2)
discount = round(full_price*discounting_factor, 2)
to_pay = full_price - discount

print("The regular price for the loaves is:  %5.2f" % full_price)
print("The discount for day old bread is:    %5.2f" % discount)
print("The total price you pay is:           %5.2f" % to_pay)