def main():

    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(string):

    if 2 <= len(string) <= 6:
        if string.isalpha():
            return True
        elif string[:2].isalpha():

            string1 = string[2:]
            for i in range(len(string1)):
                if string1[i].isdigit():
                    break
                elif not string1[i].isalpha():
                    return False

            string2 = string1[i:]
            for j in range(len(string2)):
                if not string2[j].isdigit():
                    return False
                else:
                    continue

            if string1[i] == '0':
                return False
            else:
                return True

        else:
            return False
    else:
        return False


main()
