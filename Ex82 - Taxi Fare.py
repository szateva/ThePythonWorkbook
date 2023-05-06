""" In a particular jurisdiction, taxi fares consist of a base fare of $4.00, plus $0.25 for every 140 meters traveled.
Write a function that takes the distance traveled (in kilometers) as its only parameter and returns the total fare as its
only result. Write a main program that demonstrates the function.

Hint: Taxi fares change over time. Use constants to represent the base fare and the variable portion of the fare so that
the program can be updated easily when the rates increase. """

def taxi_fare(distance):
    base_fare = 4.00
    variable_fare = 0.25
    return round(base_fare + (distance * 1000 / 140) * variable_fare, 2)

distance = float(input("Please, enter the distance traveled (km): "))
fare = taxi_fare(distance)
print(f"The total taxi fare for {distance}km is ${fare}.")