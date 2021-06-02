""" interest rate = 4% annually paid at the end of the year
 Read in deposit from the user
 compute and display the amount in the savings account after 1, 2 and 3 years
 round to 2 dp"""

deposit = float(input("What is the deposit amount? "))
interest_rate = 0.04
savings_1yr = round(deposit*(1+interest_rate), 2)
savings_2yr = round(savings_1yr*(1+interest_rate), 2)
savings_3yr = round(savings_2yr*(1+interest_rate), 2)
print("Savings after 1 yr is: ", savings_1yr)
print("Savings after 2 yr is: ", savings_2yr)
print("Savings after 3 yr is: ", savings_3yr)