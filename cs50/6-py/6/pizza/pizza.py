import sys
import csv
from tabulate import tabulate

n = len(sys.argv)

if n < 2:
    print("Too few command-line arguments")
    quit()
elif n > 2:
    print("Too many command-line arguments")
    quit()
else:
    if sys.argv[1].endswith('.csv') == False:
        print("Not a CSV file")
        quit()
    else:
        try:
            with open(sys.argv[1], 'r') as file:
                reader = csv.reader(file)

                print(tabulate(reader, headers="firstrow", tablefmt="grid"))

        except FileNotFoundError:
            print("File does not exist")
            quit()
