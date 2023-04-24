"""One of the first known examples of encryption was used by Julius Caesar. Caesar needed to provide written instructions
to his generals, but he didn’t want his enemies to learn his plans if the message slipped into their hands. As result,
he developed what later became known as the Caesar Cipher.
The idea behind this cipher is simple (and as a result, it provides no protection against modern code breaking
techniques). Each letter in the original message is shifted by 3 places. As a result, A becomes D, B becomes E,
C becomes F, D becomes G, etc. The last three letters in the alphabet are wrapped around to the beginning: X becomes A,
Y becomes B and Z becomes C. Non-letter characters are not modified by the cipher.
Write a program that implements a Caesar cipher. Allow the user to supply the message and the shift amount, and then
display the shifted message. Ensure that your program encodes both uppercase and lowercase letters. Your program should
also support negative shift values so that it can be used both to encode messages and decode messages."""

text = input("Please enter the text you would like to encrypt: ")
shift = int(input("Please enter the shift amount: "))
shifted_ascii_num = 0

for char in text:
    ascii_num = ord(char)
    if 65 <= ascii_num <= 90:
        shifted_ascii_num = (ascii_num - 65 + shift) % 26 + 65
        # calculating the letter's position in the English alphabet (where A is position 0),
        # adding the shift, and bringing the result back to the range 0-25, (so that shifted Z becomes C when shift = 3)
        # and then converting the shifted letter back to ascii
    elif 97 <= ascii_num <= 122:
        # the same as above, but for lowercase letters
        shifted_ascii_num = (ascii_num - 97 + shift) % 26 + 97
    else:
        shifted_ascii_num = ascii_num
        # if the character is not a letter, it is not shifted
    print(chr(shifted_ascii_num), end="")
