def main():

    dollars = dollars_to_float(input("How much was the meal? "))

    percent = percent_to_float(input("What percentage would you like to tip? "))

    tip = dollars * percent

    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):

    digits = list()

    for c in d:
        # check if c is digit
        if c.isdigit() or c == '.':
            # append to list: ["x", "y", ".", "x"...]
            digits.append(c)

    # intialise the number to 0
    number = 0
    for digit in digits:

        if(digit == '.'):
            number = 0
            break
        elif isinstance(int(digit), int):
           # the first digit in the list is added to the number, then multiply the number by 10 to shift it to the tenth's place, and add the second digit...so on and so forth
            number = number * 10 + int(digit)

# Unlike C, such that it's possible to store each digit as a char and printing out a string as an array of char is possible, Python do not have data-type char, it only has str.
# Hence note that the list here is a list of strings. Printing the list will output: "['x', 'y', 'z'...]"

# The join method from the 'str' class takes one argument: the sequence of strings to concatenate. The syntax for using the join method is: separator.join(sequence)
# 'separator' is the string to use to separate between the elements in the sequence and sequence is the sequence of strings to concatenate. In this case '' is None.
    number = ''.join(digits)

    dollars = float(number)

    return dollars

def percent_to_float(p):

    digits = []

    for c in p:
        if c.isdigit() or c == '.':
            digits.append(c)

    number = 0
    for digit in digits:
        if(digit == '.'):
            number = 0
            break
        elif isinstance(int(digit), int):
            number = number * 10 + int(digit)


    number = ''.join(digits)

    percent = (float(number) / 100)

    return percent

main()