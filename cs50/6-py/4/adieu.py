import inflect
p = inflect.engine()

name_list = []

while True:
    try:
        name = input("Name: ")
        name_list.append(name)
    except EOFError:
        print()
        break
    else:
        names = p.join(name_list, final_sep="")
        print(f"Adieu, adieu, to {names}")
