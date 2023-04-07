while True:
    try:
        fuel = input("Fraction: ")
        if len(fuel) != 3:
            print("Input a fraction: X/Y")
        else:
            x = float(fuel[0])
            y = float(fuel[2])

            result = (x/y) * 100
            if result >= 99:
                print('F')
                quit()
            elif result <= 1:
                print('E')
                quit()
            else:
                print(f'{result}%')
                quit()
    except (ValueError, ZeroDivisionError):
        pass
