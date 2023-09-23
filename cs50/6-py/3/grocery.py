grocery = {}

while True:
    try:
        item = input('Item: ')
        item = item.upper()

        if item in grocery:
            grocery[item] += 1
        else:
            grocery[item] = 1
    except EOFError:
        print()
        for item in grocery:
            print(f"{grocery[item]} {item}")
        break

