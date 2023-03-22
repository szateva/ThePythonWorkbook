"""
Electromagnetic radiation can be classified into one of 7 categories according to its frequency, as shown in the
table below:
        Name                Frequency range (Hz)
        Radio waves         Less than 3 x 10^9
        Microwaves          3 x 10^9 to less than 3 x 10^12
        Infrared light      3 x 10^12 to less than 4.3 x 10^14
        Visible light       4.3 x 10^14 to less than 7.5 x 10^14
        Ultraviolet light   7.5 x 10^14 to less than 3 x 10^17
        X-rays              3 x 10^17 to less than  3 x 10^19
        Gamma rays          3 x 10^ 19 or more
Write a program that reads the frequency of the radiation from the user and displays the appropriate name.
"""

radiation_freq =float(input("Please, enter the frequency of the radiation (Hz): "))

if 0 <= radiation_freq < 3*10**9:
    radiation_name = "Radio waves"
elif 3*10**9 <= radiation_freq < 3*10**12:
    radiation_name = "Microwaves"
elif 3*10**12 <= radiation_freq < 4.3*10**14:
    radiation_name = "Infrared light"
elif 4.3*10**14 <= radiation_freq < 7.5*10**14:
    radiation_name = "Visible light"
elif 7.5*10**14 <= radiation_freq < 3*10**17:
    radiation_name = "Ultraviolet light"
elif 3*10**17 <= radiation_freq < 3*10**19:
    radiation_name = "X-rays"
elif 3*10**19 <= radiation_freq:
    radiation_name = "Gamma rays"
else:
    radiation_name = ""

if radiation_name == "":
    print(f"Sorry, {radiation_freq} is not a valid frequency value.")
else:
    print(f"{radiation_freq} Hz is classified as {radiation_name}.")
