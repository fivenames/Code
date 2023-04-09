import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # Note: ...(?:to)|(?:\-)... will create two alternatives separated by the '|' symbol: ((\d+):?(\d+)? ?(?:A\.?M\.?) ?to) and (- ?(\d+):?(\d+)? ?(?:P\.?M\.?)).
    # Hence use '|' in a parenthesis as follows:
    if matches := re.search(r"^(\d+):?(\d+)? ?(?:A\.?M\.?) ?(?:to|\-) ?(\d+):?(\d+)? ?(?:P\.?M\.?)$", s, flags=re.IGNORECASE):
        morning_hour = int(matches.group(1))
        morning_min = matches.group(2)
        afternoon_hour = int(matches.group(3)) + 12
        afternoon_min = matches.group(4)

        morning, afternoon = get_time(morning_hour, afternoon_hour, morning_min, afternoon_min)

        return f"{morning} to {afternoon}"

    elif matches := re.search(r"^(\d+):?(\d+)? ?(?:P\.?M\.?) ?(?:to|\-) ?(\d+):?(\d+)? ?(?:A\.?M\.?)$", s, flags=re.IGNORECASE):
        morning_hour = int(matches.group(3))
        morning_min = matches.group(4)
        afternoon_hour = int(matches.group(1)) + 12
        afternoon_min = matches.group(2)

        morning, afternoon = get_time(morning_hour, afternoon_hour, morning_min, afternoon_min)

        return f"{afternoon} to {morning}"

    return "Unsupported time format"

def get_time(morning_hour, afternoon_hour, morning_min, afternoon_min):

        if morning_hour == 12:
            morning_hour = 0
        if afternoon_hour == 24:
            afternoon_hour = 12

        if morning_min != None:
            morning_min = int(morning_min)
            if morning_min > 59 or morning_hour > 11:
                raise ValueError
            morning = f'{morning_hour:02}{morning_min:02}'
        else:
            if morning_hour > 11:
                raise ValueError
            morning = f'{morning_hour:02}00'

        if afternoon_min != None:
            afternoon_min = int(afternoon_min)
            if afternoon_min > 59 or afternoon_hour > 23:
                raise ValueError
            afternoon = f'{afternoon_hour:02}{afternoon_min:02}'
        else:
            if afternoon_hour > 23:
                raise ValueError
            afternoon = f'{afternoon_hour:02}00'

        return morning, afternoon


if __name__ == "__main__":
    main()
