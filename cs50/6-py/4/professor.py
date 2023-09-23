import random


def main():

    level = get_level()

    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        while True:
            answer = input(f"{x} + {y} = ")

            try:
                answer = int(answer)
            except ValueError:
                print("EEE")
                continue
            if answer == (x + y):
                break
            else:
                print("EEE")
                continue

def get_level():
    while True:
        try:
            level = input("Level: ")
            level = int(level)
            if level < 1 or level > 3:
                raise ValueError
        except ValueError:
            pass
        else:
            break

    return level

def generate_integer(level):

    if level == 1:
        i = random.randint(0, 9)
    elif level == 2:
        i = random.randint(10, 99)
    else:
        i = random.randint(100, 999)

    return i

# This line makes sure that if this .py file is imported as a library to another .py file, main() is not always called.
# __name__ varaible is defined by Python to be equal to __main__ if the code itself is executed. It however, is set to the name of module when imported to other Python code.
if __name__ == "__main__":
    main()