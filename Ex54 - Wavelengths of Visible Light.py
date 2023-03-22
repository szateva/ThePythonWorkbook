"""
The wavelength of visible light ranges from 380 to 750 nanometres (nm). While the specrun is continuous, it is often
divided into 6 colours as shown below:

        Colour          Wavelength (nm)
        Violet          380 to less than 450
        Blue            450 to less than 495
        Green           495 to less than 570
        Yellow          570 to less than 590
        Orange          590 to less than 620
        Red             620 to 750
Write a program that reads a wavelength form the user and reports its colour. Display an appropriate error message
if the wavelength entered by the user is outside the visible spectrum.
"""

wave_length = int(input("Enter a wavelength in nm: "))

if 380 <= wave_length < 450:
    colour = "Violet"
elif 450 <= wave_length < 495:
    colour = "Blue"
elif 495 <= wave_length < 570:
    colour = "Green"
elif 570 <= wave_length < 590
    colour = "Yellow"
elif 590 <= wave_length < 620:
    colour = "Orange"
elif 620 <= wave_length <= 750:
    colour = "Red"
else:
    colour = ""

if colour == "":
    print(f" {wave_length} is not in the visible spectrum.")
else:
    print(f"{wave_length} is equivalent to the colour {colour} in the visible spectrum.")