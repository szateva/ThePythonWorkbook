"""
The following table contains earthquake magnitude ranges on the Richter scale and their descriptors:
        Magnitude               Descriptor
        less than 2.00          Micro
        2.0 to less than 3.0    Very minor
        3.0 to less than 4.0    Minor
        4.0 to less than 5.0    Light
        5.0 to less than 6.0    Moderate
        6.0 to less than 7.0    Strong
        7.0 to less than 8.0    Major
        8.0 to less than 10.00  Great
        10.0 or greater         Meteoric

Write a program that reads a magnitude from the user and displays the appropriate descriptor as part of a meaningful
message. For example, if the user enters 5.5 than your program should indicate that a magnitude 5.5 earthquake is
considered to be a moderate earthquake.
"""

magnitude = float(input("Please enter the magnitude of the earthquake: "))

if 0 <= magnitude < 2.0:
    descriptor = "Micro"
elif 2.0 <= magnitude < 3.0:
    descriptor = "Very minor"
elif 3.0 <= magnitude < 4.0:
    descriptor = "Minor"
elif 4.0 <= magnitude < 5.0:
    descriptor = "Light"
elif 5.0 <= magnitude < 6.0:
    descriptor = "Moderate"
elif 6.0 <= magnitude < 7.0:
    descriptor = "Strong"
elif 7.0 <= magnitude < 8.0:
    descriptor = "Major"
elif 8.0 <= magnitude < 10.0:
    descriptor = "Great"
else:
    descriptor = "Meteoric"

print(f"A magnitude {magnitude} earthquake has the descriptor {descriptor}.")