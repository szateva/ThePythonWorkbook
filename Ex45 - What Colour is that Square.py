"""
Positions on a chess board are identified by a letter and a number. The letter identifies the column, while the number
identifies the row, as shown below:
I cannot draw the board here but it is an 8 x 8 square, numbers and letters start in the bottom left corner, a1 being a
black square and every square from then on alternates between black and white.

Write a program that reads a position from the user. Use an if statement to determine if the column begins with a black
square or a white square. Then use modular arithmetic to report the colour of the square in that row. For example, if
the user enters a1 then your program should report that the square is black. If the user enters d5 then your program
should report the square is white. Your program should assume that a valid position will always be entered. It does not
need to perform any error checking.
"""

position = input("Please, enter a position on the chess board: ")

column = position[0]
row = int(position[1])

if (column == "a") or (column == "c") or (column == "e") or (column == "g"):
    if row % 2 == 1:
        colour = "black"
    else:
        colour = "white"
else:
    if row % 2 == 1:
        colour = "white"
    else:
        colour = "black"

print(f"Position {position} is a {colour} colour on the standard chess board.")


