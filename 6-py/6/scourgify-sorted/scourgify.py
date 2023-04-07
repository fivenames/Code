import sys
import csv

n = len(sys.argv)

if n < 3:
    print("Too few command-line arguments")
    quit()
elif n > 3:
    print("Too many command-line arguments")
    quit()
else:
    try:
        with open(sys.argv[1], 'r') as infile:
            reader = csv.DictReader(infile)
            newlist = []
            for row in reader:
                string = row["name"]
                first, last = string.split(',')
                newlist.append({"first" : first, "last" : last.lstrip(), "house" : row["house"]})
    except FileNotFoundError:
        print("File not found")
        quit()

# sorted() has a 'key' parameter to specify a function (or other callable) to be ***called on each element in the iterable***[done automatically by the sorted()] prior to comparing.

# Basically a function that returns the comparing element inside of each individual element in the list.
# lambda is an anonymous function, this function takes a parameter(can be called anything preferred), and returns the value of comparing element in the element.
# Hence, while passing in one dictionary at a time, and returning the house of each dictionary, the function can be defined as follows:

# def get_house(newlist[i]):
    # return newlist[i]["house"]
# newlist = sorted(newlist, key=get_house, reverse=False) works the same here. Passing in lambda indicates that the function which returns the element is not explicitly defined.

# In this context, x is the parameter representing each dictionary in the list.
newlist = sorted(newlist, key=lambda x: x["house"], reverse=False)

with open(sys.argv[2], 'w') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=['first', 'last', 'house'])
    writer.writeheader()
    for name in newlist:
        writer.writerow(name)
