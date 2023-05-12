"""A string is a palindrome if it is identical forward and backward. For example “anna”, “civic”, “level” and “hannah”
are all examples of palindromic words. Write a program that reads a string from the user and uses a loop to determine
whether or not it is a palindrome. Display the result, including a meaningful output message."""

text = input("Please enter a string: ")
is_palindrome = True
for i in range(len(text) // 2):
    # // is integer division to half the length of the string (if it's odd, the middle character is ignored)
    if text[i] != text[-i - 1]:
        # -i - 1 = -(i + 1) is the index of the character at the end of the string that corresponds to the character at index i
        is_palindrome = False
if is_palindrome == True:
    print(f"{text} is a palindrome")
else:
    print(f"{text} is not a palindrome")