""" Reading in the cost of a meal from the user.
 Calculate the tax and the tip for the meal.
 Use your local tax rate
 Tip = 18% before tax
 Output: tax amount, tip amount, total cost"""

meal = float(input("What is the cost of the meal before tax? "))
tax = float(input("what is the tax rate as a decimal? "))

tip = 0.18

tax_amount = meal * tax
tip_amount = meal * tip
total_cost = meal + tip_amount + tip_amount

print("The tax you will pay is: $%.2f" % tax_amount)
print("The tip you should pay is: $%.2f" % tip_amount)
print("The total to pay is: $%.2f" % total_cost)