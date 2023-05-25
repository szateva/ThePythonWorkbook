"""Exercise 13 (Challenge). Palindromes are words that read the same forward and backward, such
as racecar. Your task is to write a program that reads a string str given by the user and then
computes the length of the longest substring of str that is a palindrome of odd (1, 3, 5, . . .) length.

Hint: We say that the center of an odd-length palindrome is its middle position. For instance,
the center of racecar is its 3rd position (counting from 0), which stores letter e. Conceptually, the
problem can be solved as follows. Consider each possible center (using a for loop), starting with
two “fingers” pointing at the center. Then, move the fingers on opposite directions as long as the
letters they point at are identical, and as long as we have not reached a boundary of the string
in either direction. This way, we can compute the longest odd palindrome for each center. We
maintain a variable which stores the length of the longest one found so far."""

word = input("Please, enter a string: ")

longest_palindrome = 1

for i in range(1, len(word)-1):
    width = min(len(word) - 1 - i, i - 0)

    for j in range(1, width+1):

        if word[i-j] == word[i+j]:
            current_length = 2*j+1

            if current_length > longest_palindrome:
                longest_palindrome = current_length


print(f"{word} has {longest_palindrome} as the longest subset of odd length palindrome.")