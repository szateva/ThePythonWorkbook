""" An online retailer provides express shipping for many of its items at a rate of $10.95 for the first item,
and $2.95 for each subsequent item. Write a function that takes the number of items in the order as its only parameter.
Return the shipping charge for the order as the function’s result. Include a main program that reads the number of items
purchased from the user and displays the shipping charge. """

def shipping_charge(items):
    if items < 1:
        return "Invalid number of items."
    else:
        return 10.95 + (items - 1) * 2.95

items = int(input("Please, enter the number of items purchased: "))

if items < 1:
    print(f"{shipping_charge(items)}")
else:
    print(f"The shipping charge for {items} items is ${shipping_charge(items)}.")