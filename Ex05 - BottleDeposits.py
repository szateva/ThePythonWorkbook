""" In many jurisdictions a small deposit is given to drink containers to encourage people to recycle them.
 In one particular jurisdiction, drink containers holding one litre or less have a $0.10 deposit and
 drink containers holding more than one litre have a $0.25 deposit.
 Write a program that reads the number of containers of each size from the user.
 Your program should continue by computing and displaying the refund that will be received for
 returning those containers. Format the output so that it includes a dollar sign and always display
 exactly two decimal places."""

small_bottle = int(input("How many less than 1 litre bottles you have? "))
large_bottle = int(input("How many more than 1 litre bottles do you have? "))
small_deposit = 0.10
large_deposit = 0.25

small_refund = small_bottle * small_deposit
large_refund = large_bottle * large_deposit
refund = large_refund + small_refund

print("Total refund will be: $%.2f" % refund)