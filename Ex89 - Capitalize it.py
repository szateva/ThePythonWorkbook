"""Many people do not use capital letters correctly, especially when typing on small devices like smart phones. In this
exercise, you will write a function that capitalizes the appropriate characters in a string. A lowercase “i” should be
replaced with an uppercase “I” if it is both preceded and followed by a space. The first character in the string should
also be capitalized, as well as the first non-space character after a “.”, “!” or “?”. For example, if the function is
provided with the string “what time do i have to be there? what’s the address?” then it should return the string “What
time do I have to be there? What’s the address?”. Include a main program that reads a string from the user, capitalizes
it using your function, and displays the result. """

def capitalize_str(string):
    string = string.capitalize()
    #print("1", string)
    if " i " in string:
        string = string.replace(" i ", " I ")
        #print("2", string)
    elif " i." in string:
        string = string.replace(" i.", " I.")
        #print("3", string)
    elif " i!" in string:
        string = string.replace(" i!", " I!")
       # print("4", string)
    elif " i?" in string:
        string = string.replace(" i?", " I?")
        #print("5", string)
    elif ". " in string:
        for i in range(len(string)):
            if string[i] == ".":
                string = string[:i+2] + string[i+2:].capitalize()
                print("6", string)
                break
    elif "! " in string:
        for i in range(len(string)):
            if string[i] == "!":
                string = string[:i+2] + string[i+2].upper() + string[i+3:]
                print("7", string)
                break
    elif "? " in string:
        for i in range(len(string)):
            if string[i] == "?":
                string = string[:i+2] + string[i+2:].capitalize()
                print("8", string)
                break
    return string

def main():
    string = input("Please, enter a string: ")
    print(f"The correct capitalization of {string} is: {capitalize_str(string)}")

main()
