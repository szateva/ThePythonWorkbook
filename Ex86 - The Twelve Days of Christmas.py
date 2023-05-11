"""The Twelve Days of Christmas is a repetitive song that describes an increasingly long list of gifts sent to one’s true
love on each of 12 days. A single gift is sent on the first day. A new gift is added to the collection on each additional
day, and then the complete collection is sent. The first three verses of the song are shown below.

On the first day of Christmas
my true love sent to me:
A partridge in a pear tree.

On the second day of Christmas
my true love sent to me:
Two turtle doves,
And a partridge in a pear tree.

On the third day of Christmas
my true love sent to me:
Three French hens,
Two turtle doves,
And a partridge in a pear tree.

Your task is to write a program that displays the complete lyrics for The Twelve Days of Christmas. Write a function that
takes the verse number as its only parameter and displays the specified verse of the song. Then call that function 12 times
with integers that increase from 1 to 12.
Each item that is sent to the recipient in the song should only appear once in your program, with the possible exception
of the partridge. It may appear twice if that helps you handle the difference between “A partridge in a pear tree” in the
first verse and “And a partridge in a pear tree” in the subsequent verses. Import your solution to Exercise 85 to help you
complete this exercise."""

# from Ex85_list_version import ordinal_number
def ordinal_number(number):
    ordinal_numbers = ["", "first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth",
                       "ninth", "tenth", "eleventh", "twelfth"]
    if 0 < number < 13:
        return ordinal_numbers[number]
    else:
        return ordinal_numbers[0]

def repeating_lines(number):
    if number == 1:
        print("A partridge in a pear tree.")
    elif number == 2:
        print("Two turtle doves,")
    elif number == 3:
        print("Three French hens,")
    elif number == 4:
        print("Four calling birds,")
    elif number == 5:
        print("Five golden rings,")
    elif number == 6:
        print("Six geese a-laying,")
    elif number == 7:
        print("Seven swans a-swimming,")
    elif number == 8:
        print("Eight maids a-milking,")
    elif number == 9:
        print("Nine ladies dancing,")
    elif number == 10:
        print("Ten lords a-leaping,")
    elif number == 11:
        print("Eleven pipers piping,")
    elif number == 12:
        print("Twelve drummers drumming,")
def verse(number):
    # from Ex85_list_version import ordinal_number
    print(f"On the {ordinal_number(number)} day of Christmas")
    print("my true love sent to me:")
    for i in range(number, 0, -1):
        repeating_lines(i)
    print()

def main():
    for i in range(1, 13):
        verse(i)

main()