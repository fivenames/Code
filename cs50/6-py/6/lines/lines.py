import sys

n = len(sys.argv)

if n < 2:
    print("Too few command-line arguments")
    quit()
elif n > 2:
    print("Too many command-line arguments")
    quit()
else:
    if sys.argv[1].endswith('.py') == False:
        print("Not a Python file")
        quit()
    else:
        try:
            file = open(sys.argv[1], 'r')
        except FileNotFoundError:
            print("File does not exist")
            quit()
        else:
            counter = 0

for line in file:
    line = line.rstrip('\n').lstrip()
    if line.startswith('#') == False and line != '':
        counter += 1
    else:
        continue

print(counter)

file.close