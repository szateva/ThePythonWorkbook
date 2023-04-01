"""
A particular cell phone plan includes 50 minutes of air time and 50 text messages for $15.00 a month.
Each additional minute of air time costs $0.25, while additional text messages cost $0.15 each. All cell phone bills
include an additional charge of $0.44 to support 911 call centres, and the entire bill (including the 911 charge) is
subject to 5% sales tax.
"""

#TODO check if I can modify the print format to .........$12.50 so the print looks like a proper bill
#TODO ask Christine next Friday what she thinks can be done

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

additional_call_charges = additional_minutes * extra_minute_cost
additional_text_charges = additional_texts * extra_text_cost

if (additional_texts <= 0) and (additional_minutes <= 0):   # branch for no additional charges
    bill_before_tax = base_plan_cost + emergency_call_support
    tax_payable = bill_before_tax * tax
    final_bill = bill_before_tax * 1.05
    print(f"Base rate charge:.${base_plan_cost:5.2f}")
    print(f"991 call support:.${emergency_call_support:5.2f}")
    print(f"Tax:..............${tax_payable:5.2f}")
    print(f"Bill payable:.....${final_bill:5.2f}")
elif (additional_texts <= 0) and (additional_minutes > 0):  # branch for additional minutes charges but no additional texts
    bill_before_tax = base_plan_cost + emergency_call_support + additional_call_charges
    tax_payable = bill_before_tax * tax
    final_bill = bill_before_tax * 1.05
    print(f"Base rate charge:            ${base_plan_cost:.>10.2f}")
    print(f"991 call support:            ${emergency_call_support:.>10.2f}")
    print(f"Additional call charges:     ${additional_call_charges:.>10.2f}")
    print(f"Tax:                         ${tax_payable:.>10.2f}")
    print(f"Bill payable:                ${final_bill:.>10.2f}")
elif (additional_texts >= 0) and (additional_minutes <= 0): # branch for additional text charges but no additional calls
    bill_before_tax = base_plan_cost + emergency_call_support + additional_text_charges
    tax_payable = bill_before_tax * tax
    final_bill = bill_before_tax * 1.05
    print(f"Base rate charge:            ${base_plan_cost:5.2f}")
    print(f"991 call support:            ${emergency_call_support:5.2f}")
    print(f"Additional text charges:     ${additional_text_charges:5.2f}")
    print(f"Tax:                         ${tax_payable:5.2f}")
    print(f"Bill payable:                ${final_bill:5.2f}")
elif (additional_texts >= 0) and (additional_minutes >= 0): # branch for both additional text and call charges
    bill_before_tax = base_plan_cost + emergency_call_support + additional_call_charges + additional_text_charges
    tax_payable = bill_before_tax * tax
    final_bill = bill_before_tax * 1.05
    print(f"Base rate charge:            ${base_plan_cost:5.2f}")
    print(f"991 call support:            ${emergency_call_support:5.2f}")
    print(f"Additional call charges:     ${additional_call_charges:5.2f}")
    print(f"Additional text charges:     ${additional_text_charges:5.2f}")
    print(f"Tax:                         ${tax_payable:5.2f}")
    print(f"Bill payable:                ${final_bill:5.2f}")