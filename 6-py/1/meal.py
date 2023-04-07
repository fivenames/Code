def main():
    string = input("Time now is(enter in 12-hr format or 24-hr format): ")
    time = convert(string)

    if 7 < time < 20:
        if 7 < time < 8:
            print("Breakfast")
        elif 12 < time < 13:
            print("Lunch")
        elif 18 < time < 19:
            print("Dinner")
        else:
            print("Not mealtime.")
    else:
        print("Not mealtime.")


def convert(string):

    time = string.lower()

    if len(time) > 5:
        if 'a' in time and 'm' in time:
            result = []
            for c in time:
                if c.isdigit():
                    result.append(c)

            if len(result) == 3:
                time = int(result[0]) + (((int(result[1]) * 10) + int(result[2])) / 60)
                return time
            elif len(result) == 4:
                if result[0] != '0':
                    if result[0] == '1' and result[1] == '2':
                        time = 0 + (((int(result[2]) * 10) + int(result[3])) / 60)
                        return time
                    else:
                        print("Unsupported time format.")
                        quit()
                else:
                    time = int(result[1]) + (((int(result[2]) * 10) + int(result[3])) / 60)
                    return time
            else:
                print("Unsupported time format.")
                quit()
        elif 'p' in time and 'm' in time:
            result = []
            for c in time:
                if c.isdigit():
                    result.append(c)

            if len(result) == 4:
                if result[0] == '1' and result[1] == '2':
                    time = 12 + (((int(result[2]) * 10) + int(result[3])) / 60)
                    return time
                else:
                    print("Unsupported time format.")
                    quit()
            elif len(result) == 3:
                time = (int(result[0]) + 12) + (((int(result[1]) * 10) + int(result[2])) / 60)
                return time
            else:
                print("Unsupported time format.")
                quit()
        else:
            print("Unsupported time format.")
            quit()

    elif len(time) <= 5:
        if ":" in time:
            [x, y] = time.split(":")
            x = int(x)
            y = int(y)
            time = x + (y / 60)
            return time

        elif "." in time:
            [x, y] = time.split(".")
            x = int(x)
            y = int(y)
            time = x + (y / 60)
            return time

        elif len(time) == 4:
            result = list(time)
            for i in range(len(result)):
                try:
                    result[i] = int(result[i])
                except(ValueError):
                    print("Unsupported time format.")
                    quit()

            if result[0] == "0":
                time = result[1] + ((result[2]) * 10) + (result[3] / 60)
                return time
            else:
                time = ((result[0] * 10) + result[1]) + (((result[2] * 10) + result[3]) / 60)
                return time

        else:
            print("Unsupported time format.")
            quit()


if __name__ == "__main__":
    main()