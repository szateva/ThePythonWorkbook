"""Many people do not use capital letters correctly, especially when typing on small devices like smart phones. In this
exercise, you will write a function that capitalizes the appropriate characters in a string. A lowercase “i” should be
replaced with an uppercase “I” if it is both preceded and followed by a space. The first character in the string should
also be capitalized, as well as the first non-space character after a “.”, “!” or “?”. For example, if the function is
provided with the string “what time do i have to be there? what’s the address?” then it should return the string “What
time do I have to be there? What’s the address?”. Include a main program that reads a string from the user, capitalizes
it using your function, and displays the result. """

def capitalize_str(str):
    new_str = str.capitalize()
    #print("1", new_str)
    new_str = new_str.replace(" i ", " I ")
    #print("2", new_str)
    new_str = new_str.replace(" i.", " I.")
    #print("3", new_str)
    new_str = new_str.replace(" i!", " I!")
    # print("4", new_str)
    new_str = new_str.replace(" i?", " I?")
    #print("5", new_str)
    if ". " in str:
        for i in range(len(str)):
            if str[i] == ".":
                new_str = str[:i+2] + str[i+2:].capitalize()
                print("6", new_str)
                break
    elif "! " in str:
        for i in range(len(str)):
            if str[i] == "!":
                new_str = str[:i+2] + str[i+2].upper() + str[i+3:]
                print("7", new_str)
                break
    elif "? " in str:
        for i in range(len(str)):
            if str[i] == "?":
                new_str = str[:i+2] + str[i+2:].capitalize()
                print("8", new_str)
                break
    return new_str

def main():
    string = input("Please, enter a string: ")
    print(f"The correct capitalization of {string} is: {capitalize_str(string)}")

main()
