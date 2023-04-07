while True:
    try:
        height = int(input("Height: "))
        if height > 8:
            raise ValueError
    except ValueError:
        pass
    else:
        break

for i in range(height):
    print(' ' * (height - i - 1) + '#' * (i + 1) + ' ' + '#' * (i + 1))