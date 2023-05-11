"""Write a function that takes a string of characters as its first parameter, and the width of the terminal in characters
as its second parameter. Your function should return a new string that consists of the original string and the correct
number of leading spaces so that the original string will appear centered within the provided width when it is printed.
Do not add any characters to the end of the string. Include a main program that demonstrates your function."""

def center_string(string, width):
    if len(string) > width:
        return string
    else:
        spaces = (width - len(string)) // 2
        return " " * spaces + string

def main():
    string = input("Please, enter a string: ")
    width = int(input("Please, enter the width of the terminal: "))
    print(f"{center_string(string, width)}")

main()
