"""There are numerous phases that are palindromes when spacing is ignored. Examples include "go dog, "flee to me
remote elf" and "some men interpret nine memos", among many others. Extend your solution to exersice 72 so that it
ignores spacing while determining whether or not a string is a palindrome. For an additional challenge, extend your
solution so that is also ignores punctuation marks and treats uppercase and lowercase letters as equivalent."""

import string

text = input("Please enter a string: ")
# convert the text to lowercase
text = text.lower()
# pull up all punctuation marks
punctuations = string.punctuation
# Remove punctuation marks
no_punct = ""
for char in text:
    if char not in punctuations:
        no_punct += char
print(no_punct)
# Remove spaces
no_spaces = no_punct.replace(" ", "")
print(no_spaces)
is_palindrome = True
for i in range(len(no_spaces) // 2):
    # // is integer division to half the length of the string (if it's odd, the middle character is ignored)
    if no_spaces[i] != no_spaces[-i - 1]:
        # -i - 1 = -(i + 1) is the index of the character at the end of the string that corresponds to the character at index i
        is_palindrome = False
        break
if is_palindrome == True:
    print(f"{text} is a palindrome")
else:
    print(f"{text} is not a palindrome")
