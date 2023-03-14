"""
In the previous question you converted from note to frequency. In this question you will write a program that reverses
that process. Begin by reading a frequency from the user. If the frequency is within one Hertz of a value listed in the
table in the previous question then report the name of the note. Otherwise report that the frequency does not correspond
to a known note. In this exercise you only need to consider notes listed in the table. There is no need to consider notes
from other octaves.
"""
frequency = float(input("Please, type a frequency? "))

if 260.63 <= frequency <= 262.63:
    note = "C4"
elif 292.66 <= frequency <= 294.66:
    note = "D4"
elif 328.63 <= frequency <= 330.63:
    note = "E4"
elif 348.23 <= frequency <= 350.23:
    note = "F4"
elif 391.00 <= frequency <= 393.00:
    note = "G4"
elif 339.00 <= frequency <= 441.00:
    note = "A4"
elif 492.88 <= frequency <= 494.88:
    note = "B4"
else:
    note = ""

if note == "":
    print(frequency, "does not correspond to any known note.")
else:
    print(frequency, "corresponds to the note", note)