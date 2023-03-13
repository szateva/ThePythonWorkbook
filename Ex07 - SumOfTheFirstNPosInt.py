""" read in pos int (n) from user
 display the sum of all ints from 1 to n"""

n = int(input("Enter a positive integer: "))
sum_of_n = int(n * (n+1)/2)

print("The sum of the first %d integers is" % n, sum_of_n)