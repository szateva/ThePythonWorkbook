""" read the number of cents as an integer from the user
 divide into the different types of Canadian coins
 using the smallest no of coins possible"""

payment = int(input("What is the amount you want to change? "))

penny = 1
nickel = 5
dime = 10
quarter = 25
loonie = 100
toonie = 200

no_of_toonies = payment // toonie
rem_after_toonies = payment % toonie
no_of_loonies = rem_after_toonies // loonie
rem_after_loonie = rem_after_toonies % loonie
no_of_quarter = rem_after_loonie // quarter
rem_after_quarter = rem_after_loonie % quarter
no_of_dimes = rem_after_quarter // dime
rem_after_dime = rem_after_quarter % dime
no_of_nickels = rem_after_dime // nickel
no_of_pennies = rem_after_dime % nickel

print("Your change of", payment, "is equal to:")
print(no_of_toonies, "toonies")
print(no_of_loonies, "loonies")
print(no_of_quarter, "quarters")
print(no_of_dimes, "dimes")
print(no_of_nickels, "nickels and")
print(no_of_pennies, "pennies")