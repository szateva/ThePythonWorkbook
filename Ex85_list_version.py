"""Words like first, second and third are referred to as ordinal numbers. In this exercise, you will write a function
that takes an integer as its only parameter and returns a string containing the appropriate English ordinal number as its
only result. Your function must handle the integers between 1 and 12 (inclusive). It should return an empty string if a
value outside of this range is provided as a parameter. Include a main program that demonstrates your function by displaying
each integer from 1 to 12 and its ordinal number. Your main program should only run when your file has not been imported
into another program. """

# here I will use lists to store the ordinal numbers

def ordinal_number(number):
    ordinal_numbers = ["", "first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth",
                       "ninth", "tenth", "eleventh", "twelfth"]
    if 0 < number < 13:
        return ordinal_numbers[number]
    else:
        return ordinal_numbers[0]

def main():
    for i in range(1, 13):
        print(f"{i} is the {ordinal_number(i)} number.")

