"""Feburary 4, 2013 was the last day that pennies were distributed by the Royal Canadian Mint. Now that pennies have
been phased out retailers must adjust totals so that they are multiples of 5 cents when they are paid for with cash
(credit card and debit card transactions continue to be charged to the penny.) While retailers have some freedom in
how they do this, most choose to round to the closest nickel.

Write a program that reads prices from the user until a blank line is entered. Display the total cost of all the entered
items on one line, followed by the amount due if the costumer pays with cash on the second line. The amount due for cash
payments should be rounded up to the nearest nickel. One way to compute the cash payment amount is to begin by determining
how many pennies would be needed to pay the total. Then compute the remainder when this number of pennies is divided by
5. Finally, adjust the total down if the remainder is less than 2.5. Otherwise, adjust the total up."""

#TODO - create a few test cases to ensure the program works as expected

price = input("Enter the price of the item: ")
total = 0
while price != "":
    total += float(price)
    price = input("Enter the price of the item: ")
pennies = total * 100
remainder = pennies % 5
cash_payment = 0
if remainder < 2.5:
    cash_payment = (pennies - remainder) / 100
else:
    cash_payment = (pennies + (5 - remainder)) / 100
print(f"The total cost of all the items is ${total:.2f}")
print(f"The amount due if the costumer pays with cash is ${cash_payment:.2f}")