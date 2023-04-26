"""Print the prime factors of a number entered by the user."""

n = int(input("Please, enter an integer (2 or greater): "))

factor = 2
if n < 2:
    print("Sorry, the integer you entered is less than 2.")
else:
    print(f"The prime factors of {n} are:")
    while factor <= n:
        if n % factor == 0:
            print(f"{factor}")
            n = n // factor
        else:
            factor += 1