import sys
from pyfiglet import Figlet
import random

figlet = Figlet()

if len(sys.argv) == 3:
    if sys.argv[1] == '-f' or sys.argv[1] == '--font':
        fonts = figlet.getFonts()

        if sys.argv[2] in fonts:
            figlet.setFont(font=sys.argv[2])
        else:
            sys.exit("Wrong use of command-line argument.")

        string = input("Input: ")

        print(figlet.renderText(string))

    else:
        sys.exit("Wrong use of command-line argument.")

elif len(sys.argv) == 1:
    fonts = figlet.getFonts()
    b = len(fonts)
    x = random.randint(0, b - 1)

    figlet.setFont(font=fonts[x])

    string = input("Input: ")

    print(figlet.renderText(string))

else:
    sys.exit("Wrong use of command-line argument.")
