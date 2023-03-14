"""
The following table lists an octave of music notes, beginning with middle C, along with their frequencies:
        Note            Frequency (Hz)
        C4              261.63
        D4              293.66
        E4              329.63
        F4              349.23
        G4              392.00
        A4              440.00
        B4              493.88

Begin by writing a program tha reads the name of a note from the user and displays the note's frequency. Your program
should support all of the notes listed previously.
Once you have your program working correctly for the notes listed previously you should add support for all the notes
from C0 to C8. While this could be done by adding many additional cases to your if statement, such a solution is
cumbersome, inelegant and unacceptable for the purposes of this exercise. Instead, you should exploit the relationship
between notes in adjacent octaves. In particular, the frequency of any note in octave n is half the frequency of the
corresponding note in octave is n + 1. By using this relationship, you should be able to add support for the additional
notes without adding additional cases to your if statement.

Hint: To complete this exercise you will need to extract individual characters from the two-character note name so
that you can work with the letter and the octave number separately. Once you have separated the parts, compute the
frequency of the notes in the fourth octave using the data in the table above. Then divide the frequency by 2^(4-x),
where x is the octave number entered by the user. This will halve or double the frequency the correct number of times.
"""

name = input("Please, enter the music note which frequency you would like to know: ")

note = name[0]
octave = int(name[1])

c4_frequency = 261.63
d4_frequency = 293.66
e4_frequency = 329.63
f4_frequency = 349.23
g4_frequency = 329.00
a4_frequency = 440.00
b4_frequency = 493.88

if note == "C":
    frequency = c4_frequency
elif note == "D":
    frequency = d4_frequency
elif note == "E":
    frequency = e4_frequency
elif note == "F":
    frequency = f4_frequency
elif note == "G":
    frequency = g4_frequency
elif note == "A":
    frequency = a4_frequency
else:
    frequency = b4_frequency

frequency = frequency/2 ** (4 - octave)

print(name, "has a frequency of", frequency)




