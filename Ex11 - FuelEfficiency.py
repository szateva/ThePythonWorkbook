""" convert miles per gallon to litres per 100km """

mpg = float(input("What is the fuel efficiency in US mile per gallon? "))
galToLitre = 3.7854
mileTokm = 1.609344

Lper100km = (100*galToLitre)/(mileTokm*mpg)

print("The efficiency in litre per 100 km is: ", round(Lper100km, 2))