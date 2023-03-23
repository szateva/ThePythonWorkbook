"""
A particular cell phone plan includes 50 minutes of air time and 50 text messages for $15.00 a month.
Each additional minute of air time costs $0.25, while additional text messages cost $0.15 each. All cell phone bills
include an additional charge of $0.44 to support 911 call centres, and the entire bill (including the 911 charge) is
subject to 5% sales tax.

Write a program that reads the number of minutes and text messages used in a month from the user. Display the base
charge, additional charges (if any), additional text message charges (if any), the 911 fee, tax and the total bill
amount. Only display the additional minute and tax message charge if the user incurred costs in these categories.
Ensure that all of the charges are displayed using 2 decimal places.
"""

"""
There are problems withe the logic. If I calculate the bill outside the if branches, then using less than the allowance 
will calculate a smaller bill than the allowance. I will have to move the calculations inside the if branches. Also, 
the display does not adhere to the required 2 dp, I need to use the %.2f notation? How could I print .... so each amount 
is nicely lined up one under the other? (check the restaurant bill exercise!)   
"""

minute_allowance = 50
text_allowance = 50

base_plan_cost = 15.00

extra_minute_cost = 0.25
extra_text_cost = 0.15

emergency_call_support = 0.44

tax = 0.05

minutes_used = float(input("Please, enter the number of minutes of phone calls you used this months: "))
texts_used = float(input("Please, enter the number of text messages you sent this month: "))

additional_minutes = minutes_used - minute_allowance
additional_texts = texts_used - text_allowance

additional_call_charges = round(additional_minutes * extra_minute_cost, 2)
additional_text_charges = round(additional_texts * extra_text_cost, 2)

total_bill = round(base_plan_cost + emergency_call_support + additional_call_charges + additional_text_charges , 2)
tax_payable = round(total_bill * tax, 2)
final_bill = round(total_bill * 1.05, 2)

if (additional_texts <= 0) and (additional_minutes <= 0):
    print(f"Your base rate charge is ${base_plan_cost}.")
    print(f"Your 991 call centre support charge is ${emergency_call_support}.")
    print(f"Your tax is ${tax_payable}.")
    print(f"Therefore, your final bill is ${final_bill}")
elif (additional_texts <= 0) and (additional_minutes > 0):
    print(f"Your base rate charge is ${base_plan_cost}.")
    print(f"Your 991 call centre support charge is ${emergency_call_support}.")
    print(f"Your additional call charges are ${additional_call_charges}")
    print(f"Your tax is ${tax_payable}.")
    print(f"Therefore, your final bill is ${final_bill}")
elif (additional_texts >= 0) and (additional_minutes <= 0):
    print(f"Your base rate charge is ${base_plan_cost}.")
    print(f"Your 991 call centre support charge is ${emergency_call_support}.")
    print(f"Your additional text charges are ${additional_text_charges}")
    print(f"Your tax is ${tax_payable}.")
    print(f"Therefore, your final bill is ${final_bill}")
elif (additional_texts >= 0) and (additional_minutes >= 0):
    print(f"Your base rate charge is ${base_plan_cost}.")
    print(f"Your 991 call centre support charge is ${emergency_call_support}.")
    print(f"Your additional call charges are ${additional_call_charges}")
    print(f"Your additional text charges are ${additional_text_charges}")
    print(f"Your tax is ${tax_payable}.")
    print(f"Therefore, your final bill is ${final_bill}")