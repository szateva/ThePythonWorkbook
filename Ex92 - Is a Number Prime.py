"""
A prime number is an integer greater than 1 that is only divisible by one and itself. Write a function that determines
whether or not its parameter is prime, returning True if it is, and False otherwise. Write a main program that reads an
integer from the user and displays a message indicating whether or not it is prime. Ensure that the main program will not
run if the file containing your solution is imported into another program.
"""

def is_prime(number):
    if number < 2:
        return False
    else:
        for i in range(2, number):
            if number % i == 0:
                return False
        return True

def main():
    number = int(input("Please, enter an integer: "))
    if is_prime(number):
        print(f"{number} is prime.")
    else:
        print(f"{number} is not prime.")

if __name__ == "__main__":
    main()