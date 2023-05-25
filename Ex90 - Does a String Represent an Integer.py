"""In this exersice you will write a function named isInteger that determines whether or not the characters in a string
represent a valid integer. When determining if a string represents an integer you should ignore any leading or trailing
white space. Once this white space is ignored, a string represents an integer if its length is at least 1 and it only
contains digits, or if its first character is either + or - and the first character is followed by one or more characters,
all of which are digits.
Write a main program that reads a string from the user and reports whether or not it represents an integer. Ensure that
the main program will not run if the file containing your solution is imported into another program."""

def isInteger(string):
    word = string.strip()
    if word[0] == "+" or word[0] == "-":
        if word[1:].isdigit():
            return True
        else:
            return False
    elif word.isdigit():
        return True
    else:
        return False

def main():
    string = input("Please, enter a string: ")
    if isInteger(string) == True:
        print(f"{string} is an integer.")
    else:
        print(f"{string} is not an integer.")

main()