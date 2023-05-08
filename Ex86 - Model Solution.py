"""Model Solution for Ex86."""

# Imports
#from Ex85_list_version import ordinal_number

def ordinal_number(number):
    ordinal_numbers = ["", "first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth",
                       "ninth", "tenth", "eleventh", "twelfth"]
    if 0 < number < 13:
        return ordinal_numbers[number]
    else:
        return ordinal_numbers[0]
# Functions
def displayVerse(n):
    print("On the", ordinal_number(n), "day of Christmas")
    print("my true love sent to me:")
    if n >= 12:
        print("Twelve drummers drumming,")
    if n >= 11:
        print("Eleven pipers piping,")
    if n >= 10:
        print("Ten lords a-leaping,")
    if n >= 9:
        print("Nine ladies dancing,")
    if n >= 8:
        print("Eight maids a-milking,")
    if n >= 7:
        print("Seven swans a-swimming,")
    if n >= 6:
        print("Six geese a-laying,")
    if n >= 5:
        print("Five golden rings,")
    if n >= 4:
        print("Four calling birds,")
    if n >= 3:
        print("Three French hens,")
    if n >= 2:
        print("Two turtle doves,")
    if n == 1:
        print("A", end=" ")
    else:
        print("And a", end=" ")
    print("partridge in a pear tree.")
    print()

#Display all 12 verses of the song

def main():
    for verse in range(1, 13):
        displayVerse(verse)

# Call the main function
main()