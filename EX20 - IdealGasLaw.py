""" Compute the amount of gas in moles when the user supply:
 pressure (P measured in Pascal)
 volume (V measured in in litres)
 temperature (T measured in Celsius)
 use the formula PV = nRT where R = 8.314 J/(mol K)
 (rearrange to express n, the amount of substance in mol)
 this formula needs temperature in Kelvin (add 273.15 to Celsius)
 Use the following test scenario:
 V = 12 litre
 P = 20,000,000 Pascal
 T = 20 C """

temperature_C = float(input("What is the temperature of the gas in Celsius? "))
temperature_change_constant = 273.15
temperature_K = temperature_C + temperature_change_constant
R = 8.314 # ideal gas constant
pressure = float(input("What is the pressure of the gas in Pascal? "))
volume = float(input("What is the volume of the gas in litres? "))
n_mol = (pressure*volume)/(R*temperature_K)
n_mol_rounded = round(n_mol, 2)

print("The amount of gas is ", n_mol_rounded, "mol.")


