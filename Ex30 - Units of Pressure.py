"""
In this exercise you will create a program that reads a pressure from the user in kilo-pascal. Once the pressure
has been read your program should report the equivalent pressure in pound per square inch, millimeters of mercury
and atmospheres. Use your research skills to determine the conversion factors between these units.
"""

kPa = float(input("What is the pressure in kilo-Pascal? "))         #kPa is short for kiloPascal

kPa_to_atm = 0.00986923
kPa_to_psi = 0.145038
kPa_to_torr = 7.50062   #torr is the mmHg measurement's official name

psi = kPa*kPa_to_psi
torr = kPa*kPa_to_torr
atm = kPa*kPa_to_atm

print(kPa, "kPa is", round(psi,2), "psi,", round(torr,2), "torr (mmHg) and ", round(atm,2), "atm.")
