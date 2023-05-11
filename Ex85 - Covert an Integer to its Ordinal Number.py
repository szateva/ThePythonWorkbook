"""Words like first, second and third are referred to as ordinal numbers. In this exercise, you will write a function
that takes an integer as its only parameter and returns a string containing the appropriate English ordinal number as its
only result. Your function must handle the integers between 1 and 12 (inclusive). It should return an empty string if a
value outside of this range is provided as a parameter. Include a main program that demonstrates your function by displaying
each integer from 1 to 12 and its ordinal number. Your main program should only run when your file has not been imported
into another program. """

def ordinal_number(number):
    if number == 1:
        return "first"
    elif number == 2:
        return "second"
    elif number == 3:
        return "third"
    elif number == 4:
        return "fourth"
    elif number == 5:
        return "fifth"
    elif number == 6:
        return "sixth"
    elif number == 7:
        return "seventh"
    elif number == 8:
        return "eighth"
    elif number == 9:
        return "ninth"
    elif number == 10:
        return "tenth"
    elif number == 11:
        return "eleventh"
    elif number == 12:
        return "twelfth"
    else:
        return ""
def main():
    for i in range(1, 13):
        print(f"{i} is the {ordinal_number(i)} number.")

main()