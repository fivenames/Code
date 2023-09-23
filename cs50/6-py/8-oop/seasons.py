from datetime import date
from datetime import timedelta
import re
import inflect

def main():
    dob = input("Date of Birth: ")
    if matches := re.search(r"^(\d\d\d\d)\-(\d\d)\-(\d\d)$", dob):
        year = int(matches.group(1))
        month = int(matches.group(2))
        day = int(matches.group(3))

        if 0 < month < 12 or 0 < day < 31:
            dob = date(year, month, day)
            today = date.today()

            if year < today.year:
                # the date class implements __sub__, which allows operator overload
                time = today - dob
                days = time.days
                mins = days * 24 * 60

                words = inflect.engine().number_to_words(mins, andword="")
                print(f"{words} minutes")
            else:
                print('Invalid DOB')
                quit()
        else:
            print('Invalid DOB')
            quit()
    else:
        print('Invalid date format ---(YYYY-MM-DD)')
        quit()

if __name__ == "__main__":
    main()