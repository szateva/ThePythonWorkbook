""" read from the user the mass of water (m) in grams
 and the temperature change (delta_T)
 then calculate and display the total amount of energy (q) needed to achieve the temperature change
 negative q values represent energy to be taken out to cool the water"""

m = int(input("How many grams of water would you like to warm/cool? "))
delta_T = int(input("How many Celsius would you like to warm/cool the water by? "))

C = 4.186   # heat capacity of water
q = m * C * delta_T

print("To raise/lower %d grams of water by %d Celsius you will need %.2f Jules energy" %(m, delta_T, q))

""" Extension: calculate the cost of heating up the water
 use unit cost of 8.9 cents per KWh"""

electricity_unit_cost = 8.9  # cent per KWh
conversion_factor = 3600000     # Jules to KWh
energy_KWh = q / conversion_factor
cost_of_changingT = energy_KWh * electricity_unit_cost


print("To heat up/cool down %d grams of water by %d Celsius it will cost %.2f cents" % (m, delta_T, cost_of_changingT))