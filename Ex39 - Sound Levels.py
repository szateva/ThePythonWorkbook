"""
The following table list the sound level in decibels for several common noises.
        Noise           Decibel level (dB)
        Jackhammer      130
        Gas lawnmower   106
        Alarm clock     70
        Quiet room      40
Write a program that reads a sound level in decibels form the user. If the user enters a number of decibels between
the noises listed then your program should display a message indication which noises the level is between. Ensure
that your program also generates reasonable output for a value smaller tha the quietest noise in the table, and
for a value that is larger than the loudest noise in the table.
"""

noise_level = int(input("What is the noise level in dB? "))

if noise_level < 40:
    print(noise_level, "dB is quieter than a Quiet room.")
elif 40 <= noise_level < 70:
    print(noise_level, "dB is between a Quiet room and an Alarm clock.")
elif 70 <= noise_level < 106:
    print(noise_level, "dB is between an Alarm clock and a Gas lawnmower.")
elif 106 <= noise_level <130:
    print(noise_level, "dB is between a Gas lawnmower and a Jackhammer.")
else:
    print(noise_level, "dB is at least as loud as a Jackhammer!")